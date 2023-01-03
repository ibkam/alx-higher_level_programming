#!/usr/bin/python3
"""Creating a rectangle class"""


class Rectangle:
    """class Rectangle intilizing with class attributes"""
    def __init__(self, width=0, height=0):

        """setting the rectangle variables
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValuError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
