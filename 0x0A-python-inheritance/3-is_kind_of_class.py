#!/usr/bin/python3
"""class and inherited class checking function"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class
    that inherited from, the specified class ; otherwise False.
    """

    return True if isinstance(obj, a_class) else False
