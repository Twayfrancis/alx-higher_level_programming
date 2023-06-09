#!/usr/bin/python3
"""integer addition function definition"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: first int
        b: second int. defaults to 98.
    Returns:
        the sum of a and b
    Raises:
        TypeError: if a or b is not an integer or float.
    """

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    a = int(a)
    b = int(b)

    return a + b
