#!/usr/bin/python3
"""locked class definition"""


class LockedClass:
    """
    user prevented from instantianting new LockedCLass attr
    'first name'
    """

    __slots__ = ["first_name"]
