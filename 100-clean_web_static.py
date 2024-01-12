#!/usr/bin/python3
"""
Based on the file 3-deploy_web_static.py, this script deletes out-of-date
archives, using the function do_clean
"""
from fabric.api import *

env.hosts = ['54.210.106.177', '54.174.70.150']
env.user = "ubuntu"


def do_clean(number=0):
    """
    Deletes out-of-date archives

    Parameters:
        number (int): Number of archives to keep
    """
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    sudo('cd {} ; ls -t | tail -n +{} | xargs sudo rm -rf'.format(path, number))
