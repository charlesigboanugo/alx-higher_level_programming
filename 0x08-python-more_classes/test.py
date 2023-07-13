#!/usr/bin/python3
"""Define a Rectangle"""


class Rectangle():
    """A Rectangle Class"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle object with a height and width property"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width property"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height property"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"
