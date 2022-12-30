#!/usr/bin/python3
"""creating a square class"""


class Square:
    """intializing the size variable"""
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be interger")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if not self.__size:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
