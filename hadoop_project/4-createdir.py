#!/usr/bin/python2.7
"""Documentation"""
from snakebite.client import Client


def createdir(l):
    """Creates dirs listed on l withen HDFS"""
    client = Client("localhost", 9000)

    for directory in l:
        for result in client.mkdir([directory], create_parent=True):
            print(result)
