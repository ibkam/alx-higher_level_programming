#!/usr/bin/python3
"""saves to json file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a text file using json rep
    Agrs:
        @my_obj: the obj file
        @filename: the name of the file

    """
    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
