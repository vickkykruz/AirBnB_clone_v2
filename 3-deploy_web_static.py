#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:
"""

from fabric.api import local, put, run, env
from datetime import datetime
from os.path import isfile


env.hosts = ["18.214.88.2", "18.233.64.217"]
env.user = "ubuntu"


def do_pack():
    """ This function return the archive path, if archive has generated
        correctly
    """

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(date)
    archive_path = "versions/{}".format(filename)

    print("Packing web_static to {}".format(archive_path))

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.failed:
        return None

    print("Successfully packed web_static to {}".format(archive_path))


def do_deploy(archive_path):
    """ This is a function that distrubutes the archive to the webserver """

    if not isfile(archive_path):
        return False

    print("Deploying new version")

    archive_name = archive_path.split("/")[-1]
    folder_name = archive_name[: -4]
    dir_path = "/data/web_static/releases/{}".format(folder_name)

    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(dir_path))
    result = run("tar -xzf /tmp/{} -C {}".format(archive_name, dir_path))

    if result.failed:
        return False

    run("cp -r {}/web_static/* {}".format(dir_path, dir_path))
    run("rm -rf /tmp/{} {}/web_static".format(archive_name, dir_path))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(dir_path))

    print("New version deployed!")
    return True


def deploy():
    """ This is a function that perform thefull deployment from generating an
        archive in deploying
    """
    file_name = do_pack()
    if file_name is None:
        return False
    return do_deploy(filename)
