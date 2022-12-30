#!/usr/bin/python3
"""creating a square class"""


class Square:
    """intializing the class attribute"""
    def __init__(self, size=0):
        self.__size = size
    """bundling variable size with function and
        retrive variable size"""
    @property
    def size(self):
        return self.__size

    """And set it according to the value"""
    @size.setter
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an interger")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    """area of the square"""
    def area(self):
        return self.__size ** 2
