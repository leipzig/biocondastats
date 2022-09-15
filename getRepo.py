import sys
import yaml
import json
import os
import subprocess

with open(os.path.join("bioconda-recipes","recipes",sys.argv[1],"meta.yaml"),"r") as recipeyaml:
    meta = yaml.load(recipeyaml,Loader=yaml.Loader)
    if meta:
        if 'about' in meta:
            if 'home' in meta['about']:
                repo = meta['about']['home']
            elif 'dev_url' in meta['about']:
                repo = meta['about']['dev_url']
        if 'https://github.com/' in repo:
            owner = repo.replace('https://github.com/','')
            licproc = subprocess.Popen("gh api -H \"Accept: application/vnd.github+json\" /repos/{}/license".format(owner), shell=True, stdout=subprocess.PIPE).stdout
            licensestr = licproc.read()
            licensedict = json.loads(licensestr)
            if licensedict:
                if 'license' in licensedict:
                    license = (licensedict['license']['name'])
                else:
                    license = "nodict"
            else:
                license = "no json"
        else:
            license = "unknown"
        print("{}\t{}".format(repo,license))
    else:
        print("no meta\tidk")
    
    
    #{'package': {'name': None, 'version': None}, 'source': {'url': 'https://github.com/rgcgithub/regenie/archive/v.tar.gz', 'sha256': None, 'patches': ['patches/0009-update-cmake-file-for-conda.patch']}, 'build': {'number': 0}, 'requirements': {'build': [None, None, None, 'binutils >=2.33.1', 'cmake >=3.13', 'make', 'llvm-openmp', 'libgomp'], 'host': ['bgenix >=1.1.7', 'boost-cpp', 'liblapack * *mkl', 'mkl >=2020.4', 'mkl-include', 'zlib', 'zstd'], 'run': ['boost-cpp', 'mkl >=2020.4', 'sqlite', 'zlib', 'zstd']}, 'test': {'commands': ['test -f ${PREFIX}/bin/regenie', 'regenie --help', 'regenie --version']}, 'about': {'home': 'https://rgcgithub.github.io/regenie/', 'license': 'MIT', 'license_file': 'LICENSE', 'summary': 'Regenie is a C++ program for whole genome regression modelling of large genome-wide association studies (GWAS).', 'dev_url': 'https://github.com/rgcgithub/regenie', 'doc_url': 'https://rgcgithub.github.io/regenie/options/'}, 'extra': {'recipe-maintainers': ['matuskosut', 'joellembatchou']}}