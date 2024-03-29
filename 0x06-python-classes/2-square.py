#!/usr/bin/python3
"""creating a square class """


class Square:
    """ defining the square """
    def __init__(self, size=0):
        """ initializing the size attribute and making it private

        Additional argument:size be interger and more than 0"""

        if(type(size) is not int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")

        self.__size = size
