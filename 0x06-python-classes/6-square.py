#!/usr/bin/python3
"""creating a square class"""


class Square:
    """initilizing variable size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be interger")
        elif ( value < 0):
            raise ValueError("size mustbe >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if(type(value) is not tuple):
            raise TypeError("position must be atuple of 2 positive intergers")
        elif(len(value) != 2):
            raise TypeError("position must be atuple of 2 positive intergers")
        elif(type(value[0]) is not int or type(value[1]) is not int):
            raise TypeError("position must be atuple of 2 positive intergers")
        elif((value[0]) < 0) or (value[1] < 0):
            raise TypeError("position must be atuple of 2 positive intergers")
        self.__position = value
        
    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
