#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, attr_name, attr_value):
    """A function that safely adds attributes to an object"""
    if hasattr(obj, attr_name):
        raise TypeError("Can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
