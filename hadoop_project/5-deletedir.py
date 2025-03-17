#!/usr/bin/python2.7
"""documentation"""
from snakebite.client import Client


def deletedir(l):
    """removes dir listed on 'l' within HDFS"""
    client = Client("localhost", 9000)

    for directory in reversed(l):
        # recure will delete recursivly
        # this makes sure to delete even if the dir is not empty
        for result in client.delete([directory], recurse=True):
            print(result)
