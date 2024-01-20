#!/usr/bin/python3
""" locked class """


class LockedClass():
    """Prevents attribute creation unless attribute = firs_name"""
    __slots__ = ("first_name")
    def __init__(self):
        """init method"""
        pass
