#!/usr/bin/python3
""" defines A testcase class for the Square"""

import unittest

from unittest import TestCase, mock
from io import StringIO
import json
import csv


if __name__ != "__main__":
    from models.base import Base
    from models.rectangle import Rectangle
    from models.square import Square
else:
    from sys import path as syspath
    from os import path as ospath
    from pathlib import Path

    new_path = ospath.join(ospath.dirname(__file__), Path("../../"))
    new_path = ospath.abspath(new_path)
    syspath.insert(0, new_path)

    from models.base import Base
    from models.rectangle import Rectangle
    from models.square import Square


class TestBase(TestCase):
    """Tests for Base class"""

    def setUp(self):
        """ initializes environment for each unit test"""
        self.rec = Rectangle(3, 5)
        self.squ = Square(4)

    def tearDown(self):
        """ sets environment back to default for each unit test"""
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        """ tests to_json_string method """
        list_dict = [{'id': 1, 'width': 3, 'height': 5, 'x': 0, 'y': 0}]
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json.loads(json_str), list_dict)

        list_dict = [{'id': 2, 'size': 4, 'x': 0, 'y': 0}]
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json.loads(json_str), list_dict)

        list_dict = [{'id': 5, 'size': 8, 'x': 0, 'y': 5},
                     {'id': 6, 'size': 2, 'x': 5, 'y': 0}]
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json.loads(json_str), list_dict)

        list_dict = [{'id': 7, 'width': 7, 'height': 3, 'x': 0, 'y': 0},
                     {'id': 5, 'width': 2, 'height': 6, 'x': 2, 'y': 2},
                     {'id': 8, 'width': 3, 'height': 8, 'x': 0, 'y': 0}]
        json_str = Base.to_json_string(list_dict)
        self.assertEqual(json.loads(json_str), list_dict)

    def test_to_json_string_exc(self):
        """ tests to_json_string method exceptions"""
        self.assertRaises(TypeError, Base.to_json_string, "stringtest")
        self.assertRaises(TypeError, Base.to_json_string, 9)

        list_dict = [{'id': 1, 'width': 3, 'height': 5, 'x': 0, 'y': 0},
                     "stringtest"]
        self.assertRaises(TypeError, Base.to_json_string, list_dict)

        list_dict = ["stringtest", 4, None]
        self.assertRaises(TypeError, Base.to_json_string, list_dict)

        list_dict = [{'id': 1, 'width': 3, 'height': 5, 'x': 0, 'y': 0},
                     [1, 2, 3, 5, 5], {"id": 4, "width": 6, "height": 7}]
        self.assertRaises(TypeError, Base.to_json_string, list_dict)

    @mock.patch("builtins.open")
    def check_save_to_file(self, list_objs, result, obj_class, mockopen):
        """ helper for test_save_to_file unit test """
        mockopen.return_value = StringIO()
        file_stream = mockopen.return_value
        file_stream.close = lambda: None

        obj_class.save_to_file(list_objs)
        self.assertTrue(mockopen.called)
        mockopen.assert_called_once_with(obj_class.__name__ + ".json", "w")
        file_stream.seek(0)
        self.assertEqual(json.load(file_stream), result)

    def test_save_to_file(self):
        """ tests save_to_file method """
        rec = self.rec
        result = [{'id': 1, 'width': 3, 'height': 5, 'x': 0, 'y': 0}]
        self.check_save_to_file([rec], result, Rectangle)

        squ = self.squ
        result = [{'id': 2, 'size': 4, 'x': 0, 'y': 0}]
        self.check_save_to_file([squ], result, Square)

        rec = Rectangle(4, 5, x=1)
        rec1 = Rectangle(3, 6)
        result = [{'id': 3, 'width': 4, 'height': 5, 'x': 1, 'y': 0},
                  {'id': 4, 'width': 3, 'height': 6, 'x': 0, 'y': 0}]
        self.check_save_to_file([rec, rec1], result, Rectangle)

        squ = Square(8, y=5)
        squ1 = Square(2, x=5)
        result = [{'id': 5, 'size': 8, 'x': 0, 'y': 5},
                  {'id': 6, 'size': 2, 'x': 5, 'y': 0}]
        self.check_save_to_file([squ, squ1], result, Square)

        rec = Rectangle(7, 3)
        rec1 = Rectangle(2, 6, x=2, y=2, id=5)
        rec2 = Rectangle(3, 8)
        result = [{'id': 7, 'width': 7, 'height': 3, 'x': 0, 'y': 0},
                  {'id': 5, 'width': 2, 'height': 6, 'x': 2, 'y': 2},
                  {'id': 8, 'width': 3, 'height': 8, 'x': 0, 'y': 0}]
        self.check_save_to_file([rec, rec1, rec2], result, Rectangle)

        squ = Square(1)
        squ1 = Square(4, x=2, y=2)
        squ2 = Square(6, id=19)
        result = [{'id': 9, 'size': 1, 'x': 0, 'y': 0},
                  {'id': 10, 'size': 4, 'x': 2, 'y': 2},
                  {'id': 19, 'size': 6, 'x': 0, 'y': 0}]
        self.check_save_to_file([squ, squ1, squ2], result, Square)

    def test_save_to_file_exc(self):
        """ tests save_to_file method exceptions"""
        arg = self.rec
        self.assertRaises(AttributeError, Base.save_to_file, arg)

        arg = {"one": 1, "two": 2, "three": 3}
        self.assertRaises(TypeError, Square.save_to_file, arg)

        rec = Rectangle(4, 5, x=1)
        squ = Square(3, 6)
        arg = [rec, squ]
        self.assertRaises(TypeError, Rectangle.save_to_file, arg)

        rec = Rectangle(1, 6)
        tlist = [1, 2, 3, 4]
        arg = [rec, tlist]
        self.assertRaises(TypeError, Rectangle.save_to_file, arg)

    def test_from_json_string(self):
        """ tests from_json_string method """
        json_string = '[{"id": 1, "width": 3, "height": 5, "x": 0, "y": 0}]'
        res = [{"id": 1, "width": 3, "height": 5, "x": 0, "y": 0}]
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, res)

        json_string = '[{"id": 2, "size": 4, "x": 0, "y": 0}]'
        res = [{"id": 2, "size": 4, "x": 0, "y": 0}]
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, res)

        json_string = '[{"id": 7, "width": 7, "height": 3, "x": 0, "y": 0},\
                        {"id": 5, "width": 2, "height": 6, "x": 2, "y": 2},\
                        {"id": 8, "width": 3, "height": 8, "x": 0, "y": 0}]'
        res = [{"id": 7, "width": 7, "height": 3, "x": 0, "y": 0},
               {"id": 5, "width": 2, "height": 6, "x": 2, "y": 2},
               {"id": 8, "width": 3, "height": 8, "x": 0, "y": 0}]
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, res)

        json_string = '[{"id": 5, "size": 8, "x": 0, "y": 5},\
                        {"id": 6, "size": 2, "x": 5, "y": 0}]'
        obj = Base.from_json_string(json_string)
        res = [{"id": 5, "size": 8, "x": 0, "y": 5},
               {"id": 6, "size": 2, "x": 5, "y": 0}]
        obj = Base.from_json_string(json_string)
        self.assertEqual(obj, res)

    def test_from_json_string_exc(self):
        """ tests from_json_string method exceptions"""
        self.assertRaises(TypeError, Base.from_json_string, [1, 2, 3, 4])
        self.assertRaises(TypeError, Base.from_json_string, 24)
        self.assertRaises(TypeError, Base.from_json_string, {"one": 1})

    def test_create(self):
        """ tests create method"""
        squ_dict = {'id': 15, "size": 20, "x": 4, "y": 4}
        squ_inst = Square.create(**squ_dict)
        self.assertEqual(squ_inst.area(), 400)
        self.assertEqual(squ_inst.__str__(), '[Square] (15) 4/4 - 20')

        rec_dict = {'id': 1, "width": 4, "height": 7, "x": 0, "y": 0}
        rec_inst = Rectangle.create(**rec_dict)
        self.assertEqual(rec_inst.area(), 28)
        self.assertEqual(rec_inst.__str__(), '[Rectangle] (1) 0/0 - 4/7')

    def test_create_exc(self):
        """ tests create method exceptions"""
        self.assertRaises(AttributeError, Base.create, id=3)
        self.assertRaises(AttributeError, Base().create, id=4)

    def check_load_from_file(self, obj_class, json_string):
        """ helper for test_load_from_file unit test """
        mockopen = mock.mock_open(read_data=json_string)
        with mock.patch("builtins.open", new=mockopen) as mk:
            list_inst = obj_class.load_from_file()
            mk.assert_called_once_with(obj_class.__name__ + ".json", "r")

            new_dict = []
            for inst in list_inst:
                new_dict.append(inst.to_dictionary())

            self.assertEqual(json.loads(json_string), new_dict)

    def test_load_from_file(self):
        """ tests load_from_file method """
        json_string = '[{"id": 1, "width": 3, "height": 5, "x": 0, "y": 0}]'
        self.check_load_from_file(Rectangle, json_string)

        json_string = '[{"id": 2, "size": 4, "x": 0, "y": 0}]'
        self.check_load_from_file(Square, json_string)

        json_string = '[{"id": 7, "width": 7, "height": 3, "x": 0, "y": 0},\
                        {"id": 5, "width": 2, "height": 6, "x": 2, "y": 2},\
                        {"id": 8, "width": 3, "height": 8, "x": 0, "y": 0}]'
        self.check_load_from_file(Rectangle, json_string)

        json_string = '[{"id": 5, "size": 8, "x": 0, "y": 5},\
                        {"id": 6, "size": 2, "x": 5, "y": 0}]'
        self.check_load_from_file(Square, json_string)

    def check_load_csv(self, obj_class, csv_string):
        """ helper for test_load_from_file_csv unit test """
        mockopen = mock.mock_open(read_data=csv_string)
        with mock.patch("builtins.open", new=mockopen) as mk:
            list_inst = obj_class.load_from_file_csv()
            mk.assert_called_once_with(obj_class.__name__ + ".csv", "r")

            new_dict = []
            for inst in list_inst:
                new_dict.append(inst.to_dictionary())

            fieldnames_list = (csv_string.split("\n"))[0].split(",")
            fielddata = (csv_string.split("\n"))[1:]
            fielddata = ",\n".join(fielddata)
            fs = StringIO()
            writer = csv.DictWriter(fs, fieldnames_list)
            writer.writerows(new_dict)
            fs.seek(0)
            readdata = fs.read().rstrip("\r\n").split("\r")
            readdata = ",".join(readdata)
            self.assertEqual(fielddata, readdata)

    def test_load_from_file_csv(self):
        """ tests load_from_file_csv method exceptions """
        csv_string = "id,width,height,x,y\n1,3,5,0,0"
        self.check_load_csv(Rectangle, csv_string)

        csv_string = "id,size,x,y\n2,4,0,0"
        self.check_load_csv(Square, csv_string)

        csv_string = "id,width,height,x,y\n7,7,3,0,0\n5,2,6,2,2\n8,3,8,0,0"
        self.check_load_csv(Rectangle, csv_string)

        csv_string = "id,size,x,y\n5,8,0,5\n6,2,5,0"
        self.check_load_csv(Square, csv_string)

    @mock.patch("builtins.open")
    def check_save_csv(self, list_objs, result, obj_class, mockopen):
        """ helper for test_save_to_file_csv unit test """
        mockopen.return_value = StringIO()
        file_stream = mockopen.return_value
        file_stream.close = lambda: None

        obj_class.save_to_file_csv(list_objs)
        self.assertTrue(mockopen.called)
        mockopen.assert_called_once_with(obj_class.__name__ + ".csv", "w")
        file_stream.seek(0)
        header_string = file_stream.readline().rstrip("\n\r")
        csv_keys = header_string.split(",")
        reader = csv.DictReader(file_stream, csv_keys)
        list_dict = []
        for d in reader:
            list_dict.append(d)
        self.assertEqual(list_dict, result)

    def test_save_to_file_csv(self):
        """ tests save_to_file_csv method """
        rec = self.rec
        squ = self.squ
        result = [{'id': '1', 'width': '3', 'height': '5', 'x': '0', 'y': '0'}]
        self.check_save_csv([rec], result, Rectangle)

        squ = self.squ
        result = [{'id': '2', 'size': '4', 'x': '0', 'y': '0'}]
        self.check_save_csv([squ], result, Square)

        rec = Rectangle(4, 5, x=1)
        rec1 = Rectangle(3, 6)
        result = [{'id': '3', 'width': '4', 'height': '5', 'x': '1', 'y': '0'},
                  {'id': '4', 'width': '3', 'height': '6', 'x': '0', 'y': '0'}]
        self.check_save_csv([rec, rec1], result, Rectangle)

        squ = Square(8, y=5)
        squ1 = Square(2, x=5)
        result = [{'id': '5', 'size': '8', 'x': '0', 'y': '5'},
                  {'id': '6', 'size': '2', 'x': '5', 'y': '0'}]
        self.check_save_csv([squ, squ1], result, Square)

        rec = Rectangle(7, 3)
        rec1 = Rectangle(2, 6, x=2, y=2, id=5)
        rec2 = Rectangle(3, 8)
        result = [{'id': '7', 'width': '7', 'height': '3', 'x': '0', 'y': '0'},
                  {'id': '5', 'width': '2', 'height': '6', 'x': '2', 'y': '2'},
                  {'id': '8', 'width': '3', 'height': '8', 'x': '0', 'y': '0'}]
        self.check_save_csv([rec, rec1, rec2], result, Rectangle)

        squ = Square(1)
        squ1 = Square(4, x=2, y=2)
        squ2 = Square(6, id=19)
        result = [{'id': '9', 'size': '1', 'x': '0', 'y': '0'},
                  {'id': '10', 'size': '4', 'x': '2', 'y': '2'},
                  {'id': '19', 'size': '6', 'x': '0', 'y': '0'}]
        self.check_save_csv([squ, squ1, squ2], result, Square)

    def test_save_to_file_csv_exc(self):
        """ tests save_to_file_csv method exceptions"""
        arg = self.rec
        self.assertRaises(AttributeError, Base.save_to_file_csv, arg)

        arg = {"one": 1, "two": 2, "three": 3}
        self.assertRaises(TypeError, Square.save_to_file_csv, arg)

        rec = Rectangle(4, 5, x=1)
        squ = Square(3, 6)
        arg = [rec, squ]
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, arg)

        rec = Rectangle(1, 6)
        tlist = [1, 2, 3, 4]
        arg = [rec, tlist]
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, arg)

    def check_draw(self, list_rec, list_squ):
        """ helper for test_draw unit test """
        with mock.patch("turtle.Turtle") as tt:
            tpen = tt.return_value
            Base.draw(list_rec, list_squ)

            tt.assert_called_once()
            tpen.speed.assert_called_once_with(1)
            tpen.color.assert_called_once_with("white", "white")
            tpen.getscreen.assert_called_once()
            tscreen = tpen.getscreen.return_value
            tscreen.bgcolor.assert_called_once_with("black")
            tpen.left.assert_called_with(90)

            up_count = 1
            left_count = 0
            down_count = 0
            forward_count = 0
            pos_count = 0

            for inst in [*list_rec, *list_squ]:
                tpen.setpos.assert_any_call(inst.x, inst.y)
                tpen.forward.assert_any_call(inst.width)
                tpen.forward.assert_any_call(inst.height)
                up_count += 1
                left_count += 4
                down_count += 1
                forward_count += 4
                pos_count += 1

            self.assertEqual(tpen.penup.call_count, up_count)
            self.assertEqual(tpen.pendown.call_count, down_count)
            self.assertEqual(tpen.forward.call_count, forward_count)
            self.assertEqual(tpen.left.call_count, left_count)
            self.assertEqual(tpen.setpos.call_count, pos_count)

    def test_draw(self):
        """ tests draw method """
        rec = self.rec
        squ = self.squ
        self.check_draw([rec], [squ])

        rec = Rectangle(6, 6)
        rec1 = Rectangle(7, 3, x=5)
        squ = Square(10, x=3, y=3)
        squ1 = Square(9, id=14)
        self.check_draw([rec, rec1], [squ, squ1])

    def test_draw_exc(self):
        "tests for draw method exceptions"
        rec = self.rec
        squ = self.squ
        self.assertRaises(TypeError, Base.draw, "good", [squ])
        self.assertRaises(TypeError, Base.draw, [rec], "good")
        self.assertRaises(TypeError, Base.draw, ["good", rec], [squ])
        self.assertRaises(TypeError, Base.draw, [rec, rec], [squ, "good"])
        self.assertRaises(TypeError, Base.draw, None, "good")
        self.assertRaises(TypeError, Base.draw, [squ, squ], [squ, squ])
        self.assertRaises(TypeError, Base.draw, [rec], [rec])


if __name__ == "__main__":
    unittest.main()
