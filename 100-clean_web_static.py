#!/usr/bin/python3
"""
 Fabric script (based on the file 3-deploy_web_static.py) that deletes
 out-of-date archives, using the function do_clean:
"""

from fabric.api import *
import os


env.hosts = ["18.214.88.2", "18.233.64.217"]


def do_clean(number=0):
    """
    Args: number is the number of the archives, including the most recent,
        to keep.
        => If number is 0 or 1, keep only the most recent version of your
            archive.
        => if number is 2, keep the most recent, and second most recent
        versions of your archive. etc.
    """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(item)) for item in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [item for item in archives if "web_static_" in item]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(item)) for item in archives]
