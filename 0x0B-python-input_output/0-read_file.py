#!/usr/bin/python3
"""Function that reads a textfile in UTF8"""


def read_file(filename=""):
    """print the content of UTF8 file to stdout"""
    with open(filename, encoding="utf-8") as myFile:
        read_data = myFile.read()
        print(read_data, end="")