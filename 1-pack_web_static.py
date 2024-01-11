#!/usr/bin/python3
# This script generates a .tgz archive from the contents of the
# web_static folder of the AirBnB Clone repo, using the function do_pack.
from datetime import datetime
from fabric.api import local
from os import path


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
