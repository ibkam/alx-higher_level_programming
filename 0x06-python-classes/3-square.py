#!/usr/bin/python3
"""creating a class of square"""


class Square:
    """initializing the class attribute with size and setting it to private"""
    def __init__(self, size=0):

        """Arguments on variable size to be interger and more than zero"""
        if(type(size) is not int):
            raise TypeError("Size must be an interger")
        elif(size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size

        """Creating method of area"""
    def area(self):
        return self.__size ** 2
