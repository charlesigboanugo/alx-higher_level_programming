#!/usr/bin/python3
"""Defines a rectangle class"""
from .base import Base


class Rectangle(Base):
    """A rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ method of Rectangle class
        Args:
            id (int): id of rectangle object
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x-coordinate
            y (int): y-coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Rectangle width getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """Width setter
        Args:
            width (int): width of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Rectangle height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        Args:
            height (int): height of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Rectangle x getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """x-coordinate setter
        Args:
            x (int): x-coordinate of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if negative
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Rectangle y getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """y-coordinate setter
        Args:
            y (int): y-coordinate of rectangle
        Raises:
            TypeError: if not an integer
            ValueError: if negative
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Area of rectangle
        Returns:
            area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """Prints # representation of rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + self.__width * "#")

    def __str__(self):
        """Returns string representation of rectangle object"""
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y}"
                f" - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """Update attributes of Rectangle class
        Args:
            args: arguments
            kwargs: key-word arguments
        """
        size = len(args)
        if size > 0:
            self.id = args[0]
            if size > 1:
                self.width = args[1]
            if size > 2:
                self.height = args[2]
            if size > 3:
                self.x = args[3]
            if size > 4:
                self.y = args[4]
        else:
            for key in kwargs:
                if key in ["id", "width", "height", "x", "y"]:
                    self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """Dictionary representation of a rectangle
        Returns:
            dictionary of attributes
        """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}

    @staticmethod
    def desterilize_csv_dict(dictionary):
        """converts a CSV dictionary representation of Rectangle or any
           of its subclasses into a valid dictionary representation
        Returns:
            Dictionary representation of Rectangle or its any of its subclass
        Raises:
            TypeError: if dictionary is not of type dict
                       any keys or values in dictionary is not of type str
        """
        if type(dictionary) is not dict:
            raise TypeError("dictionary must be of type dict")
        for key in dictionary:
            if type(key) is not str:
                raise TypeError("invalid CSV dict key")
            if type(dictionary[key]) is not str:
                raise TypeError("invalid CSV dict key value")
        new = {}
        for key in dictionary:
            new[key] = int(dictionary[key])
        return new
