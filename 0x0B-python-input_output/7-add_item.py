#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file"""
import sys

if__name__ == "__main__":
    save_json = __import__("5-save_to_json__file").save_to_json_file
    load_json = __import__("6-load_from_json__file").load_from_json_file

    try:
        items = load_json("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_json(items, "add_item.json")
