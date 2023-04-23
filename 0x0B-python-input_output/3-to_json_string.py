#!/usr/bin/python3
"""Retuns the JSON of an object"""
import json


def to_json_string(my_obj):
    """return the JSON of an object
    Args:
        @myobj: python object

    Return: the JSON rep"""
    return json.dumps(my_obj)
