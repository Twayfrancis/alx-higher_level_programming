#!/usr/bin/python3
"""defines function that inserts a line of txt to a file"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i + 1, new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
