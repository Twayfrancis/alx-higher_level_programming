#!/usr/bin/python3
def safe_print_integer(value):
    try:
        int(value)
    except (TypeError, ValueError):
        return False
    print("{:d}".format(value))
    return True
