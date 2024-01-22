#!/usr/bin/python3
"""
Class Stuent
"""


class Student:
    """
    Define class
    """
    def __init__(self, first_name, last_name, age):
        """
        Init class
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve dictionary representation of a Student instance
        """

        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
        return {x: self.__dict__[x] for x in self.__dict__ if x in attrs}
