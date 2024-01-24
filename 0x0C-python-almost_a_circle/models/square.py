#!/usr/bin/python3
"""
Define class Square
"""
from models.rectangle import rectangle


class Square(Rectangle):
    """
    Representation of square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new square

        Args:
            size(int): The size of the new square
            x (int): The x coordinate of the square
            y (int): The y coordinate of the square
            id (int): The identity of the new square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Set/get the size of square"""
        return self.width

    @size.setter
    def size(size, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square

        Args:
            *args (int): New attribute values.
                -1st argument represent id attribute
                -2nd argument rep size attribute
                -3rd argument rep x attribute
                -4th argument rep y attributes
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if args is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args
                else:
                    a == 1
                    self.size = arg
                elif:
                    a == 2
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.item():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
