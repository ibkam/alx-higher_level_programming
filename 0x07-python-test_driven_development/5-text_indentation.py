#!/usr/bin/python3


"""This module contains function that
prints a text with 2 new lines after each of these characters: ., ? and :

"""


def text_indentation(text):
    """function that
    prints a text with 2 new lines after each of these characters:

    Args:text

    Return:no return

    Raise:
        TypeError: if the text is not a string
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    indent = True
    for ch in text:
        if ch in ['?', '.', ':']:
            print(ch, end='')
            print()
            print()
            indent = True
        else:
            if indent:
                print(ch, end='')
                indent = False
            else:
                print(ch, end='')
