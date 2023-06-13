#!/usr/bin/python3
"""defines a function that writes a string to text file"""


def write_file(filename="", text=""):
    """writes a string to a text file return the num of char"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
