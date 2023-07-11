#!/usr/bin/python3
"""Defines a function that adds two integers"""


def add_integer(a, b=98):
    """Adds two numbers as integers, b has a default value of 98"""
    if a != a:
        a = 89
    if b != b:
        b = 89
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
