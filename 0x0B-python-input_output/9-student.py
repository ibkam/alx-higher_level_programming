#!/usr/bin/python3
"""
class Student
"""


class Student:
    """
    define class
    """

    def __init__(self, first_name, last_name, age):
        """"
        init a student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieve dictionary representation of student
        """

        return self.__dict__
