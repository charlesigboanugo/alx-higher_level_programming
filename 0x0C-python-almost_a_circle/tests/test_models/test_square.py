#!/usr/bin/python3
""" defines A testcase class for the Base"""

import unittest

from unittest import TestCase, mock
from io import StringIO


if __name__ != "__main__":
    from models.square import Square
    from models.base import Base
else:
    from sys import path as syspath
    from os import path as ospath
    from pathlib import Path

    new_path = ospath.join(ospath.dirname(__file__), Path("../../"))
    new_path = ospath.abspath(new_path)
    syspath.insert(0, new_path)

    from models.square import Square
    from models.base import Base


class TestSquare(TestCase):
    """Tests for Square class"""

    def setUp(self):
        """ initializes environment for each unit test"""
        self.squ = Square(3)

    def tearDown(self):
        """ sets environment back to default for each unit test"""
        Base._Base__nb_objects = 0

    def test__init__(self):
        """ tests for proper initialization"""
        squ = self.squ
        self.assertEqual(squ.size, 3)
        self.assertEqual(squ.width, 3)
        self.assertEqual(squ.height, 3)
        self.assertEqual(squ.x, 0)
        self.assertEqual(squ.y, 0)
        self.assertEqual(squ.id, 1)

        squ = Square(6, 5)
        self.assertEqual(squ.size, 6)
        self.assertEqual(squ.x, 5)
        self.assertEqual(squ.id, 2)

        squ = Square(40, id=10)
        self.assertEqual(squ.size, 40)
        self.assertEqual(squ.id, 10)

        squ = Square(2, x=4)
        self.assertEqual(squ.size, 2)
        self.assertEqual(squ.x, 4)
        self.assertEqual(squ.id, 3)

        squ = Square(2, 4, 3, 50)
        self.assertEqual(squ.size, 2)
        self.assertEqual(squ.width, 2)
        self.assertEqual(squ.height, 2)
        self.assertEqual(squ.x, 4)
        self.assertEqual(squ.y, 3)
        self.assertEqual(squ.id, 50)

    def test__init__exceptions(self):
        """ tests improper initialization"""
        self.assertRaises(ValueError, Square, 0)
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, 2, -1, 1)
        self.assertRaises(ValueError, Square, 2, 1, -1)
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square, {})
        self.assertRaises(TypeError, Square, 3.9)
        self.assertRaises(TypeError, Square, 2, "7")
        self.assertRaises(TypeError, Square, 2, x=None)
        self.assertRaises(TypeError, Square, 2, x=[])
        self.assertRaises(TypeError, Square, 2, "3")
        self.assertRaises(TypeError, Square, 2, Y=None)
        self.assertRaises(TypeError, Square, 2, y={})

    def test_size_setter(self):
        """ tests size setter """
        squ = self.squ
        squ.size = 50

        self.assertEqual(squ.size, 50)

        with self.assertRaises(ValueError):
            squ.size = 0

        with self.assertRaises(ValueError):
            squ.size = -5

        with self.assertRaises(TypeError):
            squ.size = {}

        with self.assertRaises(TypeError):
            squ.size = "2"

        with self.assertRaises(TypeError):
            squ.size = 2.5

    def test_update(self):
        """ tests update method """
        squ = self.squ

        squ.update(89)
        self.assertEqual(squ.__str__(), "[Square] (89) 0/0 - 3")

        squ.update(89, 5)
        self.assertEqual(squ.__str__(), "[Square] (89) 0/0 - 5")

        squ.update(89, 2, 4, 5)
        self.assertEqual(squ.__str__(), "[Square] (89) 4/5 - 2")

        squ.update(size=1)
        self.assertEqual(squ.__str__(), "[Square] (89) 4/5 - 1")

        squ.update(id=16)
        self.assertEqual(squ.__str__(), "[Square] (16) 4/5 - 1")

        squ.update(size=7)
        self.assertEqual(squ.__str__(), "[Square] (16) 4/5 - 7")

        squ.update(x=1, size=10, y=20)
        self.assertEqual(squ.__str__(), "[Square] (16) 1/20 - 10")

    def test__str__(self):
        """ tests __str__ method """
        squ = self.squ
        self.assertEqual(squ.__str__(), "[Square] (1) 0/0 - 3")

        squ = Square(5, 1)
        self.assertEqual(squ.__str__(), "[Square] (2) 1/0 - 5")

        squ = Square(6, y=5, id=10)
        self.assertEqual(squ.__str__(), "[Square] (10) 0/5 - 6")

    def test_to_dictionary(self):
        """ tests to_dictionary method """
        squ = self.squ

        self.assertEqual(squ.to_dictionary(), {'x': 0, 'y': 0, 'id': 1,
                                               'size': 3})

        squ = Square(5, 3, 2)
        self.assertEqual(squ.to_dictionary(), {'x': 3, 'y': 2, 'id': 2,
                                               'size': 5})

        squ.update(x=1, size=17, y=20)
        self.assertEqual(squ.to_dictionary(), {'x': 1, 'y': 20, 'id': 2,
                                               'size': 17})


if __name__ == "__main__":
    unittest.main()
