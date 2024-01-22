#!/usr/bin/python3
"""
Function that appends a string at thi
end of a text file (UTF8) and
returns the number of characters added
"""

import json


def to_json_string(my_obj):
    """
    Returns JSON rep of an object
    """
    return json.dumps(my_obj)
