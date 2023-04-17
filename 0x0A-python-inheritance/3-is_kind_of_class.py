#!/usr/bin/python3
"""
module: Function
"""


def is_kind_of_class(obj, a_class):
    """
    A function that checks if the object is an instance of class inheritance
    """
    if isinstance(obj, a_class):
        return True
    return False
