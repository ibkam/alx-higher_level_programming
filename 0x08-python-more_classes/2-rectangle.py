#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """this represent a rectangle"""

    def __init__(self, width=0, height=0):
        """intializing rectangle class
        args:
            width: represents the rectangle width
            height: represent the rectangle height
        raises:
            TypeError: if size is not an interger
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an interger")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves heigh attributes"""
        return self.height

    @height.setter
    def height(self, value):
        """sets height attributes"""
        if not isinstance(value, int):
            raise TypeError("height must be an interger")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return(0)
        return(2 * (self.__width + self.__height))
