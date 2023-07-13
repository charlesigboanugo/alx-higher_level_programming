#!/usr/bin/python3
"""Defined a list class with member function that prints a sorted list"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints MyList, sorted"""
        print(sorted(self))
