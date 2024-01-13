#!/usr/bin/python3
"""
Based on the file 1-pack_web_static.py, this script distributes an
archive to the web servers, using the function do_deploy.
"""
from fabric.api import env, put, run
from os import path
import os

env.hosts = ['54.210.106.177', '54.174.70.150']


def do_deploy(archive_path):
    """ Deploy archive to server """
    fd = archive_path.split("/")[1]
    try:
        put(archive_path, "/tmp/{}".format(fd))
        run("mkdir -p /data/web_static/releases/{}".format(fd))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(fd, fd))
        run("rm /tmp/{}".format(fd))
        run("mv /data/web_static/releases/{}/web_static/*\
        /data/web_static/releases/{}/".format(fd, fd))
        run("rm -rf /data/web_static/releases/{}/web_static".format(fd))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/\
        /data/web_static/current".format(fd))
        print("New version deployed!")
        return True
    except Exception as e::
        print("Deployment failed!", e)
        return False
