#!/usr/bin/python3

"""
module: function
"""


def is_same_class(obj, a_class):
    """
    A function that returns True if the object is
    exactly an instance of a class; otherwise false
    """
    if type(obj) == a_class:
        return True
    return False
