#!/usr/bin/python3

"""Class defines a square."""


class Square:
    """Square """

    def __init__(self, size=0):
        """initialize the square with given size"""
        self.__size = size

    @property
    def size(self):
        """gets the size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns current square area"""
        return self.__size * self.__size
