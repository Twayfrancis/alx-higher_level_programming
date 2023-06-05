#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    """rectangle repr

    Attributes:
        number_of_instances (int): number of rectangle instances
        print_symbol (any): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, height=0, width=0):
        """rectangle initialization

        Args:
            width (int): width of new rectangle
            height (int): height of new rectangle
        """
        type(self).number_of_instances += 1
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
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Return a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Sets the del behavior of the Rectangle object."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
