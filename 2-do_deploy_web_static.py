#!/usr/bin/python3
"""
Based on the file 1-pack_web_static.py, this script distributes an
archive to the web servers, using the function do_deploy.
"""
from fabric.api import local, env, put, run, sudo
from os import path
import os

env.hosts = ['54.210.106.177', '54.174.70.150' '127.0.0.1']

def do_deploy(archive_path):
    """Distributes an archive to web servers."""
    if not path.exists(archive_path):
        return False

    try:
        filename = path.basename(archive_path).split(".")[0]
        release_path = f"/data/web_static/releases/{filename}"

        # put request for file transfer to remote servers
        put(archive_path, "/tmp/")

        # Run on remote servers
        run(f"mkdir -p {release_path}")
        run(f"tar -xzf /tmp/{path.basename(archive_path)} -C {release_path}")
        run(f"rm /tmp/{path.basename(archive_path)}")

        sudo(f"mv {release_path}/web_static/* {release_path}/")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {release_path} /data/web_static/current")

        # local() for local operations
        local(f"mkdir -p {release_path}")
        local(f"tar -xzf {archive_path} -C {release_path}")

        local(f"mv {release_path}/web_static/* {release_path}/")
        local("rm -rf /data/web_static/current")
        local(f"ln -s {release_path} /data/web_static/current")
        local(f"ln -s {release_path} /data/web_static/current")

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
