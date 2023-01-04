#!/usr/bin/python3

"""This module contains function that prints
my name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """Prints my name
    Args:
        first_name: first string
        last_name: second string
    Return:
        string with first and last name
    Raise:
        TypeError: if first_name and last_name is not a string

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
