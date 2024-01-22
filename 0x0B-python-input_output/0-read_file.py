#!/usr/bin/python3
"""
Function that reads a text file
in UTF8 and print it to stdout
"""


def read_file(filename=""):
    """
    Open file with UTF-8 and print it to stdout
    """

    with open(filename, encoding='UTF-8') as file:
        for line in file:
            print(line, end="")
