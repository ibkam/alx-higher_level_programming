#!/usr/bin/python3
"""Writes a string to a text file and return the no. of character written"""


def write_file(filename="", text=""):
    """returns the number of character written

    Args:
        @filename: the name of the file
        @text: the text to be witten
    Returns:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as myFile:
        return myFile.write(text)
