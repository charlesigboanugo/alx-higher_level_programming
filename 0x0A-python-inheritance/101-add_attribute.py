#!/usr/bin/python3
"""Defines a function that safely adds attributes to an object"""


def add_attribute(obj, name, value):
    """A function that safely adds attributes to an object"""
    if type(name) is not str:
        raise TypeError("can't add new attribute")
    try:
        exec("obj.{} = value".format(name))
    except Exception:
        raise TypeError("can't add new attribute")
