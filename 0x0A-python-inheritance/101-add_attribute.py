#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    """A function that adds a new attribute to an object if it’s possible:"""
    if type(name) is not str:
        raise TypeError("can't add new attribute")
    obj.name = value
