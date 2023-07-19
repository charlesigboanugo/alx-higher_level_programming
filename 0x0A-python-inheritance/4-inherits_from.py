#!/usr/bin/python3
"""Checks if an object is a subclass of another class"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class; otherwise False."""
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
