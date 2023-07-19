#!/usr/bin/python3
"""Module containing a function that separates sentences"""


def text_indentation(text):
    """Separates sentences in a given piece of text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    print_space = False
    for x in range(len(text)):
        if text[x] in [".", "?", ":"]:
            print(text[x], "\n", sep='')
            print_space = False
        elif text[x] == ' ':
            if print_space:
                print(' ', end='')
        else:
            print(text[x], end='')
            print_space = True
