#!/usr/bin/python3


""""
This module is composed of function that divides all elements of a maatrix

"""


def matrix_divided(matrix, div):
    """Function that divides the interger/float element of a matrix
    Args:
        matrix:a list of lists of integers or floats
        div:must be a number (integer or float)

    Return:
        A new matrix with the result of division

    Raise:
        TypeError:if element of the matrix arent lists
                  if row of the matrix are not the same size
                  if div is not an interger or float

        ZeroDivisionError: if div is equal to 0
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
