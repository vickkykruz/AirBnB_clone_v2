#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:
"""

from fabric.api import *
from datetime import datetime
import os


env.hosts = ["54.172.239.29", "54.237.98.187"]
env.user = "ubuntu"


def do_pack():
    """ This function return the archive path, if archive has generated
        correctly
    """

    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_fab_path = "versions/web_static_{}.tgz".format(date)
    tgz_archive = local("tar -cvzf {} web_static".format(archived_fab_path))

    if tgz_archive.succeeded:
        return archived_fab_path
    else:
        return None
