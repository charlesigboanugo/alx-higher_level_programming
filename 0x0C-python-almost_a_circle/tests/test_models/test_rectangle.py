#!/usr/bin/python3
""" defines A testcase class for the Rectangle"""

import unittest

from unittest import TestCase, mock
from io import StringIO


if __name__ != "__main__":
    from models.rectangle import Rectangle
    from models.base import Base
else:
    from sys import path as syspath
    from os import path as ospath
    from pathlib import Path

    new_path = ospath.join(ospath.dirname(__file__), Path("../../"))
    new_path = ospath.abspath(new_path)
    syspath.insert(0, new_path)

    from models.rectangle import Rectangle
    from models.base import Base


class TestRectangle(TestCase):
    """ tests for Rectangle class"""

    def setUp(self):
        """ initializes environment for each unit test"""
        self.rec = Rectangle(2, 4)

    def tearDown(self):
        """ sets environment back to default for each unit test"""
        Base._Base__nb_objects = 0

    def test__init__(self):
        """ tests for proper initialization"""
        rec = self.rec
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 1)

        rec = Rectangle(2, 4, 3, 5)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 5)
        self.assertEqual(rec.id, 2)

        rec = Rectangle(2, 4, id=19)
        self.assertEqual(rec.id, 19)

        rec = Rectangle(2, 4, x=4)
        self.assertEqual(rec.x, 4)
        self.assertEqual(rec.id, 3)

        rec = Rectangle(2, 4, 3, 1, 50)
        self.assertEqual(rec.width, 2)
        self.assertEqual(rec.height, 4)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 1)
        self.assertEqual(rec.id, 50)

    def test__init__exceptions(self):
        """ tests improper initialization"""
        self.assertRaises(ValueError, Rectangle, 2, 0)
        self.assertRaises(ValueError, Rectangle, 2, -1)
        self.assertRaises(ValueError, Rectangle, 0, 2)
        self.assertRaises(ValueError, Rectangle, -1, 2)
        self.assertRaises(ValueError, Rectangle, 2, 2, -1, 1)
        self.assertRaises(ValueError, Rectangle, 2, 2, 1, -1)
        self.assertRaises(TypeError, Rectangle, "2", 2)
        self.assertRaises(TypeError, Rectangle, None, 2)
        self.assertRaises(TypeError, Rectangle, {}, 2)
        self.assertRaises(TypeError, Rectangle, 2, "2")
        self.assertRaises(TypeError, Rectangle, 2, None)
        self.assertRaises(TypeError, Rectangle, 2, 3.9)
        self.assertRaises(TypeError, Rectangle, 2, 2, x="7")
        self.assertRaises(TypeError, Rectangle, 2, 2, x=None)
        self.assertRaises(TypeError, Rectangle, 2, 2, x=[])
        self.assertRaises(TypeError, Rectangle, 2, 2, y="3")
        self.assertRaises(TypeError, Rectangle, 2, 2, Y=None)
        self.assertRaises(TypeError, Rectangle, 2, 2, y={})

    def test_width_setter(self):
        """ tests width setter """
        rec = self.rec

        rec.width = 50
        self.assertEqual(rec.width, 50)

        with self.assertRaises(ValueError):
            rec.width = 0

        with self.assertRaises(ValueError):
            rec.width = -5

        with self.assertRaises(TypeError):
            rec.width = {}

        with self.assertRaises(TypeError):
            rec.width = "2"

        with self.assertRaises(TypeError):
            rec.width = 2.5

    def test_height_setter(self):
        """ tests height setter """
        rec = self.rec

        rec.height = 30
        self.assertEqual(rec.height, 30)

        with self.assertRaises(ValueError):
            rec.height = 0

        with self.assertRaises(ValueError):
            rec.height = -5

        with self.assertRaises(TypeError):
            rec.height = {}

        with self.assertRaises(TypeError):
            rec.height = "2"

        with self.assertRaises(TypeError):
            rec.height = None

    def test_x_setter(self):
        """ tests x setter """
        rec = self.rec

        rec.x = 30
        self.assertEqual(rec.x, 30)

        with self.assertRaises(ValueError):
            rec.x = -2

        with self.assertRaises(TypeError):
            rec.x = {}

        with self.assertRaises(TypeError):
            rec.x = None

        with self.assertRaises(TypeError):
            rec.x = "good"

        with self.assertRaises(TypeError):
            rec.x = 10.87

    def test_y_setter(self):
        """ tests y setter """
        rec = self.rec

        rec.y = 30
        self.assertEqual(rec.y, 30)

        with self.assertRaises(ValueError):
            rec.y = -2

        with self.assertRaises(TypeError):
            rec.y = {}

        with self.assertRaises(TypeError):
            rec.y = None

        with self.assertRaises(TypeError):
            rec.y = "good"

        with self.assertRaises(TypeError):
            rec.y = 10.87

    def test_area(self):
        """ tests area method """
        rec = self.rec
        self.assertEqual(rec.area(), 8)

        rec = Rectangle(15, 7)
        self.assertEqual(rec.area(), 105)

    def check_display(self, shape, expected_display, f):
        """ helper method for test_display unit test """
        shape.display()
        f.seek(0)
        self.assertEqual(f.read(), expected_display)
        f.seek(0)
        f.truncate()

    def test_display(self):
        """ tests display method """
        rec = self.rec

        with mock.patch("sys.stdout", new_callable=StringIO) as f:
            self.check_display(rec, "##\n##\n##\n##\n", f)

            rec = Rectangle(2, 3, 2, 2)
            self.check_display(rec, "\n\n  ##\n  ##\n  ##\n", f)

            rec = Rectangle(5, 4, 0, 4)
            self.check_display(rec, "\n\n\n\n#####\n#####\n#####\n#####\n", f)

    def test_desterilize_csv_dict(self):
        """ tests desterilize csv method """
        rec = self.rec

        dictionary = {'height': '4', 'width': '5', 'id': '89',
                      'x': '2', 'y': '0'}
        result = {'height': 4, 'width': 5, 'id': 89, 'x': 2, 'y': 0}
        self.assertEqual(rec.desterilize_csv_dict(dictionary), result)

        dictionary = {'height': '7', 'width': '1', 'id': '7'}
        result = {'height': 7, 'width': 1, 'id': 7}
        self.assertEqual(rec.desterilize_csv_dict(dictionary), result)

        with self.assertRaises(TypeError):
            rec.desterilize_csv_dict({"width": "5", "height": 4, "x": "0"})

        with self.assertRaises(TypeError):
            rec.desterilize_csv_dict({"height": "5", "id": "6", "x": [2]})

        with self.assertRaises(TypeError):
            rec.desterilize_csv_dict({"height": {"key": "test"}, "id": "6",
                                      "x": "2", "width": "8"})

    def test_update(self):
        """ tests update method """
        rec = self.rec

        rec.update(89)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 0/0 - 2/4")

        rec.update(89, 5)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 0/0 - 5/4")

        rec.update(89, 2, 3, 4, 5)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 4/5 - 2/3")

        rec.update(height=1)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 4/5 - 2/1")

        rec.update(width=5, height=7)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 4/5 - 5/7")

        rec.update(x=1, width=3, y=20)
        self.assertEqual(rec.__str__(), "[Rectangle] (89) 1/20 - 3/7")

    def test__str__(self):
        """ tests __str__ method """
        rec = self.rec
        self.assertEqual(rec.__str__(), "[Rectangle] (1) 0/0 - 2/4")

        rec = Rectangle(5, 5, 1)
        self.assertEqual(rec.__str__(), "[Rectangle] (2) 1/0 - 5/5")

        rec = Rectangle(6, 2, y=5, id=10)
        self.assertEqual(rec.__str__(), "[Rectangle] (10) 0/5 - 6/2")

    def test_to_dictionary(self):
        """ tests to_dictionary method """
        rec = self.rec

        self.assertEqual(rec.to_dictionary(), {'x': 0, 'y': 0, 'id': 1,
                                               'height': 4, 'width': 2})

        rec = Rectangle(5, 6, 3, 2)
        self.assertEqual(rec.to_dictionary(), {'x': 3, 'y': 2, 'id': 2,
                                               'height': 6, 'width': 5})

        rec.update(x=1, width=3, y=20)
        self.assertEqual(rec.to_dictionary(), {'x': 1, 'y': 20, 'id': 2,
                                               'height': 6, 'width': 3})


if __name__ == "__main__":
    unittest.main()
