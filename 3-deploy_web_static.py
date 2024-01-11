#!/usr/bin/python3
"""
Based on the file 2-do_deploy_web_static.py) that creates and distributes
an archive to the web servers, using the function deploy.
"""
from datetime import datetime
from fabric.api import local, env, put, run, sudo
from os import path
from os.path import exists

env.hosts = ['54.210.106.177', '54.174.70.150']


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    try:
        date_time_str = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = f"versions/web_static_{date_time_str}.tgz"

        if not path.exists("versions"):
            local("mkdir versions")

        local(f"tar -cvzf {archive_path} web_static")

        return archive_path

    except Exception as e:
        print(f"Error creating archive: {e}")
        return None


def do_deploy(archive_path):
    if not path.exists(archive_path):
        return False

    try:
        filename = path.basename(archive_path).split(".")[0]
        release_path = "/data/web_static/releases/{}".format(filename)

        print("Basename", path.basename(archive_path))
        put(archive_path, "/tmp/")

        sudo("mkdir -p {}".format(release_path))
        sudo("tar -xzf /tmp/{} -C {}".format(path.basename(archive_path), release_path))
        sudo("rm /tmp/{}".format(path.basename(archive_path)))

        # Move contents of the extracted archive to the release path
        sudo('mv {}/web_static/* {}/'.format(release_path, release_path))

        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(release_path))

        return True
    except Exception as e:
        print("Exception: {}".format(e))
        return False


def deploy():
    """
    Creates and distributes an archive to web servers.

    Returns:
        True if deployment is successful, False otherwise.
    """
    archive_path = do_pack()

    if archive_path is None:
        return False

    return do_deploy(archive_path)
