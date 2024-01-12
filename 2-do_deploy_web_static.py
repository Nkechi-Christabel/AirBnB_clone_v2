#!/usr/bin/python3
"""
Based on the file 1-pack_web_static.py, this script distributes an
archive to the web servers, using the function do_deploy.
"""
from fabric.api import env, put, run, sudo
from os import path

env.hosts = ['54.210.106.177', '54.174.70.150']


def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False

    try:
        filename = path.basename(archive_path).split(".")[0]
        release_path = "/data/web_static/releases/{}".format(filename)

        print("Basename", path.basename(archive_path))
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(path.basename(archive_path),
                                            release_path))
        run("rm /tmp/{}".format(path.basename(archive_path)))

        sudo('mv {}/web_static/* {}/'.format(release_path, release_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        print("Exception: {}".format(e))
        return False
