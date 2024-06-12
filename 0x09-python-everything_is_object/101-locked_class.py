#!/usr/bin/python3
"""Module containing a class with locked down attributes"""


class LockedClass:
    """Class with locked down attributes. instances Can only add first_name"""

    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(f"'{self.__class__.__name__}'\
 object has no attribute '{name}'")
        else:
            self.__class__.first_name = value        
