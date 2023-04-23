#!/usr/bin/python3
"""module: Function"""
import json


def load_from_json_file(filename):
    """creates an obj froim a json file

    Args:
        @filename: the name of the file
    """
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.loads(myFile.read())
