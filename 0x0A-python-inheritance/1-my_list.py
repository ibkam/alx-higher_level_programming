#!/usr/bin/python3

"""
module: mylist
"""


class MyList(list):
    """
    subclass mylist of parent list class
    """
    def print_sorted(self):
        """
        print a sorted list
        """
        print(sorted(self))
