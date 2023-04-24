#!/usr/bin/python3
"""modue:class student"""


class Student():
    """Rep a student"""
    def __init__(self, first_name, last_name, age):
        """Intialize a new Student
        Args:
            @first_name: the first name
            @second_name: the second name
            @age: the age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
     def to_json(self):
        return self.__dict__
