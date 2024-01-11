#!/usr/bin/python3
# Based on the file 1-pack_web_static.py, this script distributes an
# archive to your web servers, using the function do_deploy.
from fabric.api import env, put, run, sudo
from os import path
from os.path import exists

env.hosts = ['54.210.106.177', '54.174.70.150']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/<archive filename without extension>/
        archive_filename = archive_path.split('/')[-1]
        archive_name = archive_filename.split('.')[0]
        release_path = '/data/web_static/releases/{}'.format(archive_name)

        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Delete the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        run('rm -f {}'.format(current_link))

        # Create a new symbolic link pointing to the new version of the code
        run('ln -s {} {}'.format(release_path, current_link))

        return True

    except Exception as e:
        print(e)
        return False
