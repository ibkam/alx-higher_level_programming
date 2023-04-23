#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file

    Args:
        @filename: the name of the file
        @text: the text to be appended

    Returns: the number of characters
    """
    with open(filename, "a", encoding="utf-8") as myFile:
        return myFile.write(text)
