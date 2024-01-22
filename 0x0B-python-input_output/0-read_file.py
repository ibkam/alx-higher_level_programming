#!/usr/bin/python3


def read_file(filename=""):
    """
    Function that reads a text file
    in UTF8 and print it to stdout
    """

    with open(filename, encoding='UTF-8') as file:
        for line in file:
            print(line, end="")
