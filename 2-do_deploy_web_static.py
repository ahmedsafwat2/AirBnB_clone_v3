#!/usr/bin/python3
"""import libraries"""
from fabric.api import *
from datetime import datetime

env.hosts = ["54.174.242.67", "54.173.71.78"]
env.user = "ubuntu"


def do_pack():
    """generate tgz"""
    try:
        local("mkdir -p versions")
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        arch_name = "web_static_{}.tgz".format(time)
        local("tar -cvzf versions/{} web_static".format(arch_name))
        return ("versions/{}".format(arch_name))
    except Exception:
        return None


def do_deploy(archive_path):
    """deploy website"""
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put("{}".format(archive_path), "/tmp/")
        run("sudo mkdir -p {}{}".format(path, no_ext))
        run("sudo tar -xzf /tmp/{} -C {}{}/".format(file_n, path, no_ext))
        run("sudo rm /tmp/{}".format(file_n))
        run("sudo mv {}{}/web_static/* {}{}/".format(
            path, no_ext, path, no_ext))
        run("sudo rm -rf {}{}/web_static".format(path, no_ext))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}{}/ /data/web_static/current".format(path, no_ext))
        return True
    except Exception:
        return False
