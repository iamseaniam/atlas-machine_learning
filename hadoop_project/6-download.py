#!/usr/bin/python2.7
"""Documentation"""
from snakebite.client import Client


def download(l):
    """retrieves HDFS files listed in 'l' and stores them in /tmp"""
    client = Client("localhost", 9000)

    for dir in l:
        for result in client.copyToLocal(['/holbies/input/lao.txt'], '/tmp'):
            print(result)
