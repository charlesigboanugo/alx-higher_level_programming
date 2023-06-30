#!/usr/bin/python3
""" Defines a square class """


class square:
    """ A square class """

    def __init__(self, size):
        self.__size = size

    def get_size(self):
        return self.__size


my_square = square(2)
print(my_square.__dict__)
print(my_square.__doc__)
print(my_square.get_size())
