#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence) == "":
        First_character = None
    else:
        First_character = sentence[0]
    return (len(sentence), First_character)
