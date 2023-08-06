#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2018-22 SHS-AV s.r.l. (<http://ww.zeroincombenze.it>)
#
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
#
#    All Rights Reserved
#
from __future__ import print_function, unicode_literals
from builtins import input
import argparse
import sys
import os
from time import sleep
from z0lib import z0lib

try:
    from wget_odoo_repositories import main as get_list_from_url
except ImportError:
    from wok_code.scripts.wget_odoo_repositories import main as get_list_from_url
try:
    from clodoo.clodoo import build_odoo_param
except ImportError:
    from clodoo import build_odoo_param


__version__ = "2.0.1"

ODOO_VALID_VERSIONS = (
    "16.0",
    "15.0",
    "14.0",
    "13.0",
    "12.0",
    "11.0",
    "10.0",
    "9.0",
    "8.0",
    "7.0",
    "6.1",
)

ODOO_VALID_GITORGS = ('oca', 'librerp', 'zero')

DEFAULT_DATA = {
    "librerp12": {
        "PATH": "~/12.0",
        "URL": "git@github.com:LibrERP-network",
        "CONFN": "odoo12.conf",
        "addons_kalamitica": "",
        "addons_nardo": "",
        "aeroo_reports": "",
        "connector-prestashop": "https://github.com/LibrERP",
        "custom-addons": "git@github.com:LibrERP",
        "deploy": "git@gitlab.com:powerp1",
        "double-trouble": "git@github.com:LibrERP",
        "fixed_modules": "",
        "generic": "",
        "profiles": "",
        "warehouse-logistics-stock": "git@gitlab.com:/powerp1",
        "zerobug-test": "git@github.com:zeroincombenze",
    },
    "librerp14": {
        "PATH": "~/14.0",
        "URL": "git@github.com:LibrERP-network",
        "CONFN": "odoo14.conf",
        "custom-addons": "git@github.com:LibrERP",
        "deploy": "git@gitlab.com:powerp1",
        "double-trouble": "git@github.com:LibrERP",
        "generic": "git@gitlab.com:powerp1",
        "profiles": "",
        "warehouse-logistics-stock": "git@gitlab.com:/powerp1",
        "zerobug-test": "git@github.com:zeroincombenze",
    },
    "librerp6": {
        "PATH": "~/librerp6",
        "URL": "https://github.com/iw3hxn",
        "CONFN": "odoo6-librerp.conf",
    },
    "oca14": {
        "zerobug-test": "",
    },
}
INVALID_NAMES = ["addons", "debian", "doc", "egg-info", "oca", "odoo"]


class OdooDeploy(object):

    def __init__(self, opt_args):
        self.opt_args = opt_args
        self.git_org = opt_args.git_orgs[0] if opt_args.git_orgs else 'oca'
        self.root = opt_args.target_dir
        self.addons_path = []
        self.result = {}
        self.DATA = {}
        for git_org in ODOO_VALID_GITORGS:
            for branch in ODOO_VALID_VERSIONS:
                if git_org == 'librerp' and branch not in ('12.0', '14.0'):
                    continue
                hash_key = git_org + branch.split(".")[0]
                if git_org == self.opt_args.default_gitorg:
                    odoo_vid = branch
                else:
                    odoo_vid = hash_key
                self.DATA[hash_key] = {}
                if hash_key in DEFAULT_DATA:
                    for key, item in DEFAULT_DATA[hash_key].items():
                        self.DATA[hash_key][key] = item
                if self.root:
                    self.DATA[hash_key]['PATH'] = self.root
                elif 'PATH' not in self.DATA[hash_key]:
                    self.DATA[hash_key]['PATH'] = build_odoo_param(
                        "ROOT", odoo_vid=odoo_vid, multi=True)
                if "URL" not in self.DATA[hash_key]:
                    if git_org == 'zero':
                        self.DATA[hash_key]["URL"] = "git@github.com:zeroincombenze"
                    elif git_org == 'oca':
                        self.DATA[hash_key]["URL"] = "https://github.com/OCA"
                    elif git_org == 'librerp':
                        self.DATA[hash_key]["URL"] = "git@github.com:LibrERP-network"
                    if opt_args.config:
                        self.DATA[hash_key]['CONFN'] = opt_args.config
                    elif 'CONFN' not in self.DATA[hash_key]:
                        self.DATA[hash_key]['CONFN'] = os.path.basename(
                            build_odoo_param("CONFN", odoo_vid=odoo_vid, multi=True))

    def run_traced(self, cmd):
        return z0lib.run_traced(cmd,
                                verbose=self.opt_args.verbose,
                                dry_run=self.opt_args.dry_run)

    def print_result(self, result=None):
        result = result or self.result
        maxlen = {'repo': 0, 'org': 0, 'sts': 3, 'path': 0, 'branch': 0}
        for repo in result.keys():
            maxlen["repo"] = max(maxlen["repo"], len(repo))
            for item in ('org', 'path', 'branch'):
                maxlen[item] = max(maxlen[item], len(result[repo][item]))
        linelen = sum([x for x in maxlen.values()])
        for item in ('repo', 'org', 'sts', 'path', 'branch'):
            maxlen[item] = int(maxlen[item] * 80 / linelen) + 1
        fmt = ""
        for item in ('repo', 'org', 'sts', 'path', 'branch'):
            fmt += "%%-%d.%ds " % (maxlen[item], maxlen[item])
        for repo in sorted(result.keys()):
            print(fmt % (repo,
                         result[repo]['org'],
                         result[repo]['sts'],
                         result[repo]['path'],
                         result[repo]['branch'],))

    def list_data(self):
        for git_org in ODOO_VALID_GITORGS:
            if self.opt_args.git_orgs and git_org in self.opt_args.git_orgs:
                continue
            for branch in ODOO_VALID_VERSIONS:
                if self.opt_args.odoo_branch and branch != self.opt_args.odoo_branch:
                    continue
                hash_key = git_org + branch.split(".")[0]
                if hash_key not in self.DATA:
                    continue
                print('[%s]' % hash_key)
                if hash_key in sorted(self.DATA.keys()):
                    for key in ('CONFN', 'PATH', "URL"):
                        if key in self.DATA[hash_key]:
                            print('  %-12.12s = "%s"' % (key, self.DATA[hash_key][key]))
                    for key, item in sorted(self.DATA[hash_key].items()):
                        if key in ('CONFN', 'PATH', "URL"):
                            continue
                        print('    %-20.20s = "%s"' % (key, item))

    def find_data_dir(self, canonicalize=None):
        tgtdir = os.path.join(os.environ['HOME'], ".local")
        if os.path.isdir(tgtdir):
            tgtdir = os.path.join(tgtdir, "share")
            if not os.path.isdir(tgtdir) and canonicalize:
                os.mkdir(tgtdir)
            odoo_master_branch = build_odoo_param(
                "FULLVER", odoo_vid=self.opt_args.odoo_branch, multi=True)
            base = 'Odoo%s' % odoo_master_branch.split('.')[0]
            tgtdir = os.path.join(tgtdir, base)
            if not os.path.isdir(tgtdir) and canonicalize:
                os.mkdir(tgtdir)
            for base in ('addons', 'filestore', 'sessions'):
                tgt = os.path.join(tgtdir, base)
                if not os.path.isdir(tgt) and canonicalize:
                    os.mkdir(tgt)
            tgtdir = os.path.join(tgtdir, 'addons')
        return tgtdir

    def update_gitignore(self, repos):
        if repos:
            tgtdir = self.get_path_of_repo('OCB')
            content = ''
            gitignore_fn = os.path.join(tgtdir, '.gitignore')
            if os.path.isfile(gitignore_fn):
                with open(gitignore_fn, "r") as fd:
                    content = fd.read()
            updated = False
            for repo in repos:
                if repo == "OCB":
                    continue
                if ('\n%s\n' % repo) in content or ('\n/%s\n' % repo) in content:
                    continue
                content += ('/%s\n' % repo)
                updated = True
            if updated and not self.opt_args.dry_run:
                with open(gitignore_fn, "w") as fd:
                    fd.write(content)

    def update_conf(self, addons_path=None, git_org=None, branch=None):
        addons_path = addons_path or self.addons_path
        if addons_path:
            data_dir = self.find_data_dir(canonicalize=True)
            git_org = git_org or self.git_org
            branch = branch or self.opt_args.odoo_branch
            hash_key = git_org + branch.split(".")[0]
            if hash_key not in self.DATA:
                for git_org in self.opt_args.git_orgs:
                    hash_key = git_org + branch.split(".")[0]
                    if hash_key in self.DATA:
                        break
            if hash_key in self.DATA:
                config_file = os.path.join("/etc/odoo",
                                           self.DATA[hash_key]["CONFN"])
                with open(config_file, "r") as fd:
                    content = fd.read()
                config = ''
                for ln in content.split("\n"):
                    if ln.startswith("addons_path"):
                        ln = 'addons_path = %s' % ','.join(addons_path)
                    elif ln.startswith("data_dir"):
                        ln = 'data_dir = %s' % data_dir
                    config += ('%s\n' % ln)
                if not self.opt_args.dry_run:
                    with open(config_file, "w") as fd:
                        fd.write(config)

    def is_git_repo(self, repo):
        res = bool(repo)
        if repo:
            if repo.startswith('.') or repo.startswith('_'):
                res = False
            elif repo in INVALID_NAMES:
                res = False
            elif self.root:
                tgtdir = self.get_path_of_repo(repo)
                res = os.path.isdir(os.path.join(tgtdir, '.git'))
        return res

    def get_alt_gitorg(self, git_org=None):
        git_org = git_org or self.git_org
        return {
            'odoo': 'oca',
            'librerp': 'zero',
            'zero': 'oca',
        }.get(git_org)

    def explore_root_dir(self, repos):
        if self.root:
            for repo in os.listdir(self.root):
                if self.is_git_repo(repo) and repo not in repos:
                    repos.append(repo)
        return repos

    def repo_is_ocb(self, repo):
        return repo in ("OCB", "odoo")

    def get_path_of_repo(self, repo):
        if self.repo_is_ocb(repo):
            tgtdir = self.root
        else:
            tgtdir = os.path.join(self.root, repo)
        return tgtdir

    def get_remote_info(self):
        branch = url = None
        sts2, stdout, stderr = self.run_traced("git branch")
        if stdout:
            for ln in stdout.split("\n"):
                if ln.startswith("*"):
                    branch = ln[2:]
                    break
        sts2, stdout, stderr = self.run_traced("git remote -v")
        if stdout:
            for ln in stdout.split("\n"):
                lns = ln.split()
                if lns[0] == "origin":
                    url = lns[1][:-4]
                    break
        return branch, url

    def list_repo_info(self, git_org=None, branch=None):
        git_org = git_org or self.git_org
        branch = branch or self.opt_args.odoo_branch
        hash_key = git_org + branch.split(".")[0]
        repos = []
        if hash_key not in self.DATA:
            return repos
        self.root = os.path.expanduser(self.DATA[hash_key]['PATH'])
        repos = self.explore_root_dir(repos)
        self.result = {}
        for repo in repos:
            tgtdir = self.get_path_of_repo(repo)
            self.run_traced("cd %s" % tgtdir)
            self.result[repo] = {
                'sts': 0,
                'path': tgtdir,
                'org': git_org,
                'branch': branch,
            }
            branch, url = self.get_remote_info()
            if branch:
                self.result[repo]['branch'] = branch
            if url:
                self.result[repo]['org'] = url.split(":")[-1].split("/")[0]

    def get_root_from_addons(self, repos, git_org=None, branch=None):
        git_org = git_org or self.git_org
        branch = branch or self.opt_args.odoo_branch
        hash_key = git_org + branch.split(".")[0]
        dirnames = {}
        HOME = os.environ["HOME"]
        with open("/etc/odoo/%s" % self.DATA[hash_key]["CONFN"], "r") as fd:
            content = fd.read()
        for ln in content.split("\n"):
            if ln.startswith("addons_path"):
                value = ln.split("=")[1].strip()
                for path in value.split(","):
                    if not path.startswith(HOME):
                        print("Path %s outside user root!" % path)
                        continue
                    repo = os.path.basename(path)
                    if not self.is_git_repo(repo):
                        repos.append(repo)
                        dname = os.path.dirname(path)
                        if dname not in dirnames:
                            dirnames[dname] = 0
                        dirnames[dname] += (2 if repo == 'addons' else 1)
                break
        root = False
        ctr = 0
        for dname in dirnames.keys():
            if dirnames[dname] > ctr:
                root = dname
                ctr = dirnames[dname]
        return root, repos

    def get_repo_info(self, git_org=None, branch=None, only_ocb=None):
        git_org = git_org or self.git_org
        branch = branch or self.opt_args.odoo_branch
        hash_key = git_org + branch.split(".")[0]
        repos = []
        if hash_key not in self.DATA:
            return repos
        with_ocb = False
        if self.opt_args.create_new:
            opts = []
            if self.opt_args.verbose:
                opts.append('-v')
            if self.opt_args.dry_run:
                opts.append('-D')
            if branch:
                opts.append('-b')
                opts.append(branch)
            opts.append('-l')
            opts.append('l10n-italy,l10n-italy-supplemental')
            opts.append('-G')
            opts.append(
                {
                    'zero': 'zeroincombenze',
                    'oca': 'OCA'
                }.get(git_org, git_org)
            )
            opts.append('--return-repos')
            if only_ocb:
                content = ['OCB']
            else:
                content = get_list_from_url(opts)
            self.root = os.path.expanduser(self.DATA[hash_key]['PATH'])
            for repo in content:
                if self.repo_is_ocb(repo):
                    with_ocb = True
                    continue
                repos.append(repo)
        elif self.opt_args.only_update:
            if hash_key not in self.DATA:
                return []
            self.root = os.path.expanduser(self.DATA[hash_key]['PATH'])
            repos = self.explore_root_dir(repos)
            if repos:
                with_ocb = True
        else:
            root, repos = self.get_root_from_addons(
                repos, git_org=git_org, branch=branch)
            if root:
                self.root = root
            if self.opt_args.update_addons_conf:
                repos = self.explore_root_dir(repos)
            if repos:
                with_ocb = True
        if with_ocb:
            repos = ['OCB'] + sorted(repos)
        else:
            repos = sorted(repos)
        return repos

    def download_single_repo(self, repo, git_org=None, branch=None):
        git_org = git_org or self.git_org
        branch = branch or self.opt_args.odoo_branch
        odoo_master_branch = build_odoo_param("FULLVER", odoo_vid=branch, multi=True)
        hash_key = git_org + branch.split(".")[0]
        tgtdir = self.get_path_of_repo(repo)
        if self.opt_args.only_update:
            if not os.path.isdir(tgtdir):
                return 127
            if os.getcwd() != tgtdir:
                self.run_traced("cd %s" % tgtdir)
            repo_branch, git_url = self.get_remote_info()
            repo = git_url.split("/")[-1]
            git_url = "/".join(git_url.split("/")[0:-1])
        elif self.repo_is_ocb(repo) and not self.opt_args.keep_root_owner:
            git_url = 'https://github.com/odoo'
            repo = 'odoo'
        elif repo in self.DATA[hash_key]:
            git_url = self.DATA[hash_key][repo]
        else:
            git_url = self.DATA[hash_key]["URL"]
        if not git_url:
            return 127
        if not git_url.endswith(".git"):
            git_url = "%s/%s.git" % (git_url, repo)
        bakdir = ''
        if os.path.isdir(tgtdir) and not self.opt_args.only_update:
            if self.opt_args.skip_if_exist:
                return self.git_pull(tgtdir, branch, master_branch=odoo_master_branch)
            elif not self.opt_args.assume_yes:
                print("Path %s of repo %s already exists!" % (tgtdir, repo))
                dummy = input("Delete (y/n)? ")
                if not dummy.lower().startswith("y"):
                    return 3
            if self.repo_is_ocb(repo):
                bakdir = '%s~' % tgtdir
                if os.path.isdir(bakdir):
                    cmd = "rm -fR %s" % bakdir
                    self.run_traced(cmd)
                cmd = "mv %s %s" % (tgtdir, bakdir)
                self.run_traced(cmd)
            else:
                cmd = "rm -fR %s" % tgtdir
                self.run_traced(cmd)
        if os.path.isdir(tgtdir) and self.opt_args.only_update:
            sts = self.git_pull(tgtdir, branch, master_branch=odoo_master_branch)
            self.result[repo] = {
                'sts': sts,
                'path': tgtdir,
                'org': git_org,
                'branch': branch,
            }
        else:
            sts = self.git_clone(
                git_url, tgtdir, branch,
                master_branch=odoo_master_branch,
                compact=True if git_org in ('odoo', 'oca') else False)
            self.result[repo] = {
                'sts': sts,
                'path': tgtdir,
                'org': git_org,
                'branch': branch,
            }
            if not os.path.isdir(tgtdir) and not self.opt_args.dry_run:
                sts = 1
            if os.path.isdir(tgtdir) or self.opt_args.dry_run:
                cmd = "cd %s" % tgtdir
                self.run_traced(cmd)
            if os.path.isdir(tgtdir):
                if self.repo_is_ocb(repo) and bakdir and os.path.isdir(bakdir):
                    for fn in os.listdir(bakdir):
                        if fn.startswith('.') or fn.startswith('_'):
                            continue
                        path = os.path.join(bakdir, fn)
                        tgtfn = os.path.join(tgtdir, fn)
                        if os.path.exists(tgtfn):
                            continue
                        if os.path.isdir(path):
                            cmd = "mv %s/ %s/" % (path, tgtfn)
                            self.run_traced(cmd)
                        else:
                            cmd = "mv %s %s" % (path, tgtfn)
                            self.run_traced(cmd)
        if os.path.isdir(tgtdir) or repo == "OCB" or self.opt_args.dry_run:
            self.add_addons_path(tgtdir, repo)
            branch, url = self.get_remote_info()
            if branch:
                self.result[repo]['branch'] = branch
            if url:
                self.result[repo]['org'] = url.split(":")[-1].split("/")[0]
        if sts:
            print("*** Error ***")
            if not self.opt_args.verbose:
                dummy = input("Press RET to continue ...")
        return sts

    def use_alt_branch(self, cmd, branch, master_branch):
        sts = 1
        if branch.endswith("-devel"):
            sts, stdout, stderr = self.run_traced(cmd.replace("-devel", "_devel"))
        elif branch.endswith("_devel"):
            sts, stdout, stderr = self.run_traced(cmd.replace("_devel", "-devel"))
        if sts and master_branch and branch != master_branch:
            cmd = cmd.replace(branch, master_branch)
            sts, stdout, stderr = self.run_traced(cmd)
        return sts

    def add_addons_path(self, tgtdir, repo):
        if self.repo_is_ocb(repo):
            path = ""
            for base in ('odoo', 'openerp'):
                if os.path.isdir(os.path.join(tgtdir, base)):
                    path = os.path.join(tgtdir, base, 'addons')
                    break
            if path:
                self.addons_path.append(path)
            self.addons_path.append(os.path.join(tgtdir, 'addons'))
            self.addons_path.append(self.find_data_dir())
        else:
            self.addons_path.append(tgtdir)

    def git_clone(self, git_url, tgtdir, branch, master_branch=None, compact=None):
        root = os.path.dirname(tgtdir)
        base = os.path.basename(tgtdir)
        if os.getcwd() != root:
            cmd = "cd %s" % root
            self.run_traced(cmd)
        if git_url.startswith("git"):
            opts = "-b %s" % branch
        elif compact:
            opts = "-b %s --depth=1 --single-branch" % branch
        else:
            opts = "-b %s --depth=1 --no-single-branch" % branch
        if opts:
            cmd = "git clone %s %s/ %s" % (git_url, base, opts)
        else:
            cmd = "git clone %s %s/" % (git_url, base)
        sts, stdout, stderr = self.run_traced(cmd)
        if self.opt_args.dry_run and 'devel' in branch:
            sts = 1
        if sts:
            sts = self.use_alt_branch(cmd, branch, master_branch)
        if sts:
            print("Invalid branch %s" % branch)
        return sts

    def git_pull(self, tgtdir, branch, master_branch=None):
        if os.getcwd() != tgtdir:
            self.run_traced("cd %s" % tgtdir)
        cmd = "git stash"
        self.run_traced(cmd)
        sleep(1)
        cmd = "git checkout %s" % branch
        sts, stdout, stderr = self.run_traced(cmd)
        if sts:
            sleep(1)
            sts = self.use_alt_branch(cmd, branch, master_branch)
        if sts:
            print("Invalid branch %s" % branch)
        sleep(1)
        cmd = "git pull"
        return self.run_traced(cmd)[0]


def repo_of_gitorg(
    opt_args, deploy, repos, addons_path, result, git_org, only_ocb=None
):
    loaded_repos = []
    for repo in repos:
        if repo == 'OCB' and not only_ocb:
            continue
        elif repo != 'OCB' and only_ocb:
            continue
        deploy.download_single_repo(repo, git_org=git_org)
        loaded_repos.append(repo)
    if loaded_repos:
        addons_path = addons_path + deploy.addons_path
        for repo in deploy.result.keys():
            if repo not in result or deploy.result.get('sts', 255) == 0:
                result[repo] = deploy.result[repo]
        deploy.update_gitignore(loaded_repos)
    opt_args.target_dir = deploy.root
    return deploy, repos, addons_path, result


def main(cli_args=None):
    cli_args = cli_args or sys.argv[1:]
    parser = argparse.ArgumentParser(
        description="Deploy Odoo repositories from git",
        epilog="© 2021-2022 by SHS-AV s.r.l."
    )
    parser.add_argument('-A', '--update-addons-conf',
                        action='store_true',
                        help='Update addons_path in Odoo configuration file')
    parser.add_argument('-b', '--odoo-branch', dest='odoo_branch', default="12.0")
    parser.add_argument('-c', '--config',
                        help='Odoo configuration file')
    parser.add_argument('-D', '--default-gitorg', default='zero')
    parser.add_argument('-e', '--skip-if-exist', action='store_true')
    parser.add_argument('-G', '--git-orgs',
                        help='Git organizations, comma separated - '
                             'May be: oca librerp or zero')
    parser.add_argument('-K', '--keep-root-owner',
                        action='store_true',
                        help='keep OCB/odoo organization owner')
    parser.add_argument('-L', '--list',
                        action='store_true',
                        help='List configuration data')
    parser.add_argument('-N', '--create-new',
                        action='store_true',
                        help='create all repositories of organization')
    parser.add_argument('-n', '--dry-run', action='store_true')
    parser.add_argument('-O', '--link-oca',
                        action='store_true',
                        help='link to more OCA repositories')
    parser.add_argument('-R', '--reclone',
                        action='store_true',
                        help='reclone existent repositories')
    parser.add_argument('-S', '--status',
                        action='store_true',
                        help='List repositoy info')
    parser.add_argument('-t', '--target-dir',
                        help='Local directory')
    parser.add_argument('-U', '--only-update',
                        action='store_true',
                        help='update (pull) repositories')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-V', '--version', action="version", version=__version__)
    parser.add_argument('-y', '--assume-yes', action='store_true')
    opt_args = parser.parse_args(cli_args)

    opt_args.git_orgs = opt_args.git_orgs.split(',') if opt_args.git_orgs else []
    if opt_args.list:
        deploy = OdooDeploy(opt_args)
        deploy.list_data()
        return 0
    elif opt_args.status:
        deploy = OdooDeploy(opt_args)
        deploy.list_repo_info()
        deploy.print_result()
        return 0

    odoo_master_branch = build_odoo_param(
        "FULLVER", odoo_vid=opt_args.odoo_branch, multi=True)
    if odoo_master_branch not in ODOO_VALID_VERSIONS:
        print("Invalid odoo version")
        exit(1)
    if opt_args.only_update:
        if opt_args.git_orgs:
            print("Invalid git organization issued when update!")
            exit(1)
    else:
        for git_org in opt_args.git_orgs:
            if git_org not in ODOO_VALID_GITORGS:
                print("Invalid git organization: %s" % git_org)
                exit(1)
    if not opt_args.only_update and not opt_args.create_new and not opt_args.reclone:
        print("No action issued! Please use -U or -N or -R switch")
        exit(1)
    if ((opt_args.only_update and opt_args.create_new)
            or (opt_args.create_new and opt_args.reclone)
            or (opt_args.only_update and opt_args.reclone)):
        print("Too switches -U or -N or -R!")
        exit(1)
    if not opt_args.git_orgs:
        opt_args.git_orgs = [
            build_odoo_param(
                "GIT_ORGID", odoo_vid=opt_args.odoo_branch, multi=True)
        ]

    addons_path = []
    result = {}
    deploys = {}
    for git_org in opt_args.git_orgs:
        deploys[git_org] = {}
        deploy = OdooDeploy(opt_args)
        repos = deploy.get_repo_info(git_org=git_org)
        deploy, repos, addons_path, result = repo_of_gitorg(
            opt_args, deploy, repos, addons_path, result, git_org, only_ocb=True)
        deploys[git_org]['obj'] = deploy
        deploys[git_org]['repos'] = repos
        addons_path = []

    if 'OCB' not in result:
        git_org = 'oca'
        deploys[git_org] = {}
        deploy = OdooDeploy(opt_args)
        repos = deploy.get_repo_info(git_org=git_org, only_ocb=True)
        deploy, repos, addons_path, result = repo_of_gitorg(
            opt_args, deploy, repos, addons_path, result, git_org, only_ocb=True)
        deploys[git_org]['obj'] = deploy
        deploys[git_org]['repos'] = repos

    for git_org in opt_args.git_orgs:
        deploy = deploys[git_org]['obj']
        repos = deploys[git_org]['repos']
        deploy, repos, addons_path, result = repo_of_gitorg(
            opt_args, deploy, repos, addons_path, result, git_org, only_ocb=False)
        opt_args.skip_if_exist = True

    if opt_args.link_oca:
        for git_org in deploys.keys():
            if git_org not in ("odoo", "oca"):
                break
        tgtroot = deploys[git_org]['obj'].root
        git_org = 'oca'
        deploys[git_org] = {}
        deploy = OdooDeploy(opt_args)
        branch = deploy.opt_args.odoo_branch
        # hash_key = git_org + branch.split(".")[0]
        deploy.root = build_odoo_param(
            "ROOT", odoo_vid=branch, multi=True, git_org="oca")
        repos = deploy.explore_root_dir([])
        for repo in repos:
            if repo == "OCB":
                continue
            srcdir = deploy.get_path_of_repo(repo)
            tgtdir = os.path.join(tgtroot, os.path.basename(srcdir))
            if not os.path.isdir(tgtdir):
                deploy.run_traced("ln -s %s %s" % (srcdir, tgtdir))

    if opt_args.verbose and addons_path:
        print('addons_path = %s' % ','.join(addons_path))
    if opt_args.update_addons_conf:
        deploy.update_conf(addons_path=addons_path)
    if opt_args.verbose:
        deploy.print_result(result=result)


if __name__ == "__main__":
    exit(main())
