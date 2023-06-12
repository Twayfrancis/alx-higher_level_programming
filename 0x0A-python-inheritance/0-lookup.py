#!/usr/bin/python3

"""object attribute lookup function definition"""


def lookup(obj):
    """Returns a list of the available attributes and methods of an object.

    Args:
        obj: The object to lookup.

    Returns:
        list of strings, each string is name of attribute or method of object
    """

    return dir(obj)
