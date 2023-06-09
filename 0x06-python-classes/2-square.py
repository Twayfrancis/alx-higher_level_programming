#!/usr/bin/python3

""" This class represents a square."""


class Square:
    """A square"""

    def __init__(self, size=0):
        """Initializes the square with a given size.

        Args:
            size (int): The size of the new square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")

        self.__size = size

    def area(self):
        """square area present"""
        return self.__size * self.__size
