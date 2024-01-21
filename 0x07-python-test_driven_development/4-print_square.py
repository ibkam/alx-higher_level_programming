#!/usr/bin/python3
"""Contains definition of print_square() function"""


def print_square(size):
    """Prints a square of size 'size' using the '#' character.
    Args:
        size (int): length of one side of the square.
            Must be a positive integer.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            print('#' * size) 
