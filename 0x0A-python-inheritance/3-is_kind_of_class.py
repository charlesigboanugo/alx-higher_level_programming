#!/usr/bin/python3
"""Defines a function to check if object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or
    class a_class inherits from"""
    return (isinstance(obj, a_class))
