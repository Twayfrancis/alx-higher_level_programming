#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """rectangle repr"""

    def __init__(self, height=0, width=0):
        """rectangle initialization

        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """ rectangle height setting"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ rectangle width setting"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
