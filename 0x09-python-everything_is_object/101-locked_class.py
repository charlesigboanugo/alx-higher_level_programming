#!/usr/bin/python3
"""Module containing a class with locked down attributes"""


class LockedClass:
    """Class with locked down attributes. Can only add first_name"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'LockedClass' object has \
no attribute '{name}'")
        else:
            super().__setattr__(name, value)

    def __getattr__(self, name):
        if name == '__dict__':
            raise AttributeError(f"'LockedClass' object has \
no attribute '{name}'")
        else:
            return super().__getattr__(name)
