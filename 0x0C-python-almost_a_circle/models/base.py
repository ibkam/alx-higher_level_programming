#!/usr/bin/python3
"""
Define a base class
"""


class Base:
    """
    Base Model class
    Private class attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Init the class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
