#!/usr/bin/python3
"""defines a function that appends a string at end of txt file"""


def append_write(filename="", text=""):
    """appends a string at end of txt file and returns num of char"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
