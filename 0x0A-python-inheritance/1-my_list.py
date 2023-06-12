#!/usr/bin/python3
""" creates a class inheriting list class"""


class MyList(list):
    """ inherits from list"""
    def print_sorted(self):
        """prints the list"""
        sorted_list = sorted(self)
        print(sorted_list)
