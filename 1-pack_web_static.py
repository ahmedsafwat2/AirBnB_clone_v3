#!/usr/bin/python3
"""import libraries"""
from fabric.api import *
from datetime import datetime


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
