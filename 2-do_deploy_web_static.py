#!/usr/bin/python3
"""
Based on the file 1-pack_web_static.py, this script distributes an
archive to the web servers, using the function do_deploy.
"""
from fabric.api import env, put, run, sudo
from os import path
from os.path import exists

env.hosts = ['54.210.106.177', '54.174.70.150']


def do_deploy(archive_path):
    """deploy web static with fabric"""
    if exists(archive_path) is False:
        return False

    try:
        filename = archive_path.split("/")[-1]
        no_excep = filename.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}{}/'.format(path, no_excep))
        run('sudo tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_excep))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}{1}/web_static/* {0}{1}/'.format(path, no_excep))
        run('sudo rm -rf {}{}/web_static'.format(path, no_excep))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}{}/ /data/web_static/current'.format(path, no_excep))
        return True
    except BaseException:
        return False
