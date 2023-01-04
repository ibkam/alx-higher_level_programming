#!/usr/bin/python3


""" This module contains function that prints a square with
the character #
"""


def print_square(size):
    """function that prints a square

    Args:size

    Return: printed sqaure with the character #

    Raise:
        TypeError: if size is float and less than 0
        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
