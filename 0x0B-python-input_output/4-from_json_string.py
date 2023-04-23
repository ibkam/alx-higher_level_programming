#!/usr/bin/python3
"""Defines json rep to python obj"""
import json


def from_json_string(my_str):
    """returns python obj from json

    Agrs:
        @my_str: json strin
    Returns: python object
    """
    return json.loads(my_str)
