#!/usr/bin/python3
"""
Based on the file 3-deploy_web_static.py, this script deletes out-of-date
archives, using the function do_clean
"""
from fabric.api import env, run, local, lcd, cd
from datetime import datetime
import os

env.hosts = ['54.210.106.177', '54.174.70.150']


def do_clean(number=0):
    """
    Deletes out-of-date archives

    Parameters:
        number (int): Number of archives to keep
    """
    number = int(number)

    if number < 0:
        number = 0
    elif number == 1:
        number = 1
    else:
        number = number + 1

    with lcd('./versions'):
        local('ls -t | tail -n +{} | xargs rm -f'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))

    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number))

    print('Cleaned up old versions')


if __name__ == "__main__":
    do_clean()
