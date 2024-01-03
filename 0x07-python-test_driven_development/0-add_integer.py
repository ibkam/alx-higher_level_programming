#!/usr/bin/python3
"""
    This module defines addition function of two integers
"""


def add_integer(a, b=98):
    """
    Function that adds two integers and float numbers

    Args:
        a:First number
        b:Second number

    Return:
        Addition of a and b

    Raise TypeError:
        When a or b or both are not integers or float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
