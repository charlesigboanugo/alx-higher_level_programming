#!/usr/bin/python3
""" Defines a square class """
from .rectangle import Rectangle


class Square(Rectangle):
    """A square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """__init__ method of Square class
        Args:
            size (int): size of square
            x (int): x-coordinate
            y (int): y-coordinate
            id (int): id of square object
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Square getter method"""
        return self.width

    @size.setter
    def size(self, size):
        """Size setter
        Args:
            size (int): size of square
        Raises:
            TypeError: if not an integer
            ValueError: if not greater than zero
        """
        self.width = size
        self.height = size

    def __str__(self):
        """String representation of square object"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """Update attributes
        Args:
            args: arguments
            kwargs: key-word arguments
        """
        size = len(args)
        if size > 0:
            self.id = args[0]
            if size > 1:
                self.size = args[1]
            if size > 2:
                self.x = args[2]
            if size > 3:
                self.y = args[3]
        else:
            for key in kwargs:
                if key in ["id", "size", "x", "y"]:
                    self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """Dictionary representation of object
        Returns:
            dictionary of attributes
        """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
