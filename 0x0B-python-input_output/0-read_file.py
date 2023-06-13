#!/usr/bin/python3
"""defines a function that rreads a text file
    and prints to stdout:"""


def read_file(filename=""):
    """ reads a text file and prints it to stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
