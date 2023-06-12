#!/usr/bin/python3

"""object attribute lookup function definition"""


def lookup(obj):
    """Returns a list of the available attributes and methods of obj"""
    return dir(obj)
