#!/usr/bin/python3
"""
Define a rectnagle class
"""
from base import Base


class Rectangle(Base):
    """
    Represent a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle

        Args:
            width (int): The width of the new Rectangle
            height (int): The height of the new Rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The identity of the new Rectangle
        Raises:
            TypeError: if either of width or height is not an int
            TypeError: if either of width or height <= 0
            TypeErrror: if either of x or y is not an int
            ValueError: if either of x or y < 0
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """set width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError(
