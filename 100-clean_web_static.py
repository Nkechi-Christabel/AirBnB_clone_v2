#!/usr/bin/python3
"""
Based on the file 3-deploy_web_static.py, this script deletes out-of-date
archives, using the function do_clean
"""
env.hosts = ['54.210.106.177', '54.174.70.150']


def do_clean(number=0):
    """Deletes out-of-date archives."""

    # Clean local versions folder
    try:
        local("ls -t versions | tail -n +{number} | xargs rm -rf")
    except Exception as e:
        print(f"Error cleaning local archives: {e}")

    # Clean remote releases folders
    try:
        run("ls -t /data/web_static/releases | tail -n +{number} | xargs rm -rf")
    except Exception as e:
        print(f"Error cleaning remote archives: {e}")
