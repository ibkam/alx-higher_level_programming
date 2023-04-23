#!/usr/bin/python3
"""Define a class rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using Basegeometry"""

    def __init__(self, width, height):
        """intialize a new rectangle

        Args:
            width (int): the width of the new rectangle.
            height (int): the height of the new rectangle.
        """

        self.integer_validator("width", width)
        self._width = width
        self.integer_validator("height", height)
        self._height = height
