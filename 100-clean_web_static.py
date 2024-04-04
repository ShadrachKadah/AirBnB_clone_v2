#!/usr/bin/python3
<<<<<<< HEAD
"""
A Fabric script (based on the file 3-deploy_web_static.py)
that deletes out-of-date archives, using the function do_clean
"""
import os
from fabric.api import cd, env, local, run

env.hosts = ["34.231.110.206", "3.239.57.196"]


def do_clean(number=0):
    """
    Deletes out-of-date archives
    Args:
        number: is the number of the archives, including the most recent
    """
    n = 1 if int(number) == 0 else int(number)
    files = [f for f in os.listdir('./versions')]
    files.sort(reverse=True)
    for f in files[n:]:
        local("rm -f versions/{}".format(f))
    remote = "/data/web_static/releases/"
    with cd(remote):
        tgz = run(
            "ls -tr | grep -E '^web_static_([0-9]{6,}){1}$'"
        ).split()
        tgz.sort(reverse=True)
        for d in tgz[n:]:
            run("rm -rf {}{}".format(remote, d))
=======
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["100.25.156.223", "34.227.93.103"]


def do_clean(number=0):
    """Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
>>>>>>> a9fe34ecaf215ca72d84256baacbc86bc6faa8cd
