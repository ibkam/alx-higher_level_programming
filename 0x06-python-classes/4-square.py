#!/usr/bin/python3
"""creating a square class"""


class Square:
    """A class of Squaree"""

    def __init__(self, size=0):
        """intializing class Square
        Arg:
            size: size of the sqaure
        Raise:
            TypeError: if size is not interger
            ValueError: if size is less than zero
        """

        self.size = size

    @property
    def size(self):
        """retrieve size attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets size attributes"""
        if(type(value) is not int):
            raise TypeError("size must be an interger")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns area of the square"""
        return self.__size ** 2
