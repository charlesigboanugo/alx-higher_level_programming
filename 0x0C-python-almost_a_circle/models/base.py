#!/usr/bin/python3
"""defines a base class"""
import json
import csv
import turtle


class Base:
    """base class for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method for Base class
        Args:
            id (int): id for object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON string of object dictionary
        Args:
            list_dictionaries (list): list of dictionaries
        Returns:
            JSON string representation of list of dictionary
        Raises:
            TypeError:
                if list_dictionaries is not a list
                if list_dictionaries is not a list of only dict
        """
        if list_dictionaries is None:
            return '[]'
        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list")
        for i in list_dictionaries:
            if type(i) is not dict:
                raise TypeError("list_dictionaries must be a list of dict")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file - saves objects to a JSON file
        Args:
            list_objs (list): list of objects
        Raises:
            AttributeError: if cls has no "to_dictionary" method (save_to_file
                            is called by object that has no to_dictionary
                            method)
            TypeError:
                if list_objs is not a list
                if list_objs is not a list of only instances of cls
        """
        if not hasattr(cls, "to_dictionary"):
            raise AttributeError(f'{cls.__name__} has no "to_dictionary" attri'
                                 'bute. "save_to_file" can only be used by a'
                                 'class which defines the "to_dictionary"'
                                 'method')
        filename = f"{cls.__name__}.json"
        list_dict = []
        if list_objs is not None:
            if type(list_objs) is not list:
                raise TypeError("list_objs must be a list")
            for obj in list_objs:
                if type(obj) is not cls:
                    raise TypeError(f"list_objs must be a list of objects"
                                    f" which are instances of {cls.__name__}")
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        json_string = cls.to_json_string(list_dict)
        with open(filename, "w") as f:
            json.dump(list_dict, f)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string - creates list of the JSON string representation
        Args:
            json_string (str): JSON string of object
        Returns:
            list of JSON string
        Raises:
            TypeError: if json_string is not a string
        """
        if json_string is None:
            return []
        if type(json_string) is not str:
            TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes set
        Args:
            dictionary (dict): dictionary of attributes and values
        Returns:
            instance of an object initialized
        Raises:
            AttributeError: if cls has no update attribute
        """
        if not hasattr(cls, "update"):
            raise AttributeError(f'{cls.__name__} has no "update" attribute.'
                                 ' "create" can only be used by a class which'
                                 ' defines the "update" method')
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """load_from_file - creates a list of instances from JSON file
        Returns:
            list of instances
        """
        list_objs = []
        list_dict = []
        filename = f'{cls.__name__}.json'
        try:
            with open(filename, "r") as f:
                json_str = f.read()
                list_dict = cls.from_json_string(json_str)
        except FileNotFoundError:
            print("file not found")
            return list_objs
        for d in list_dict:
            inst = cls.create(**d)
            list_objs.append(inst)
        return list_objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save_to_file - saves objects to a CSV file
        Args:
            list_objs (list): list of objects
        Raises:
            AttributeError: if cls has no "to_dictionary" method (save_to_
                            file_csv is called by object that has no
                             to_dictionary method)
            TypeError:
                if list_objs is not a list
                if list_objs is not a list of only instances of cls
        """
        if not hasattr(cls, "to_dictionary"):
            raise AttributeError(f'{cls.__name__} has no "to_dictionary"'
                                 'attribute. "save_to_file" can only be'
                                 'used by a class which defines the'
                                 '"to_dictionary" method')
        filename = f"{cls.__name__}.csv"
        list_dict = []
        csv_keys = []
        if list_objs is not None:
            if type(list_objs) is not list:
                raise TypeError("list_objs must be a list")
            for obj in list_objs:
                if type(obj) is not cls:
                    raise TypeError(f"list_objs must be a list of objects"
                                    f" which are instances of {cls.__name__}")
                csv_keys = list(obj.to_dictionary())
            for obj in list_objs:
                list_dict.append(obj.to_dictionary())
        with open(filename, "w") as f:
            writer = csv.DictWriter(f, csv_keys)
            writer.writeheader()
            writer.writerows(list_dict)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file - creates a list of instances from CSV file
        Returns:
            list of instances
        """
        list_objs = []
        list_dict = []
        csv_keys = []
        filename = f'{cls.__name__}.csv'
        try:
            with open(filename, "r") as f:
                header_string = f.readline().rstrip("\n")
                csv_keys = header_string.split(",")
                reader = csv.DictReader(f, csv_keys)
                for x in reader:
                    x = cls.desterilize_csv_dict(x)
                    list_dict.append(x)
        except FileNotFoundError:
            print("file not found")
            return list_objs
        for d in list_dict:
            inst = cls.create(**d)
            list_objs.append(inst)
        return list_objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw - opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): list of Rectangle instances
            list_squares (list): list of Square instances
        Raises:
            TypeError:
                if list_rectangles is not a list
                if list_squares is not a list
                if list_rectangles is not a list of only instances of Rectangle
                if list_squares is not a list of only instances of Square
        """
        if type(list_rectangles) is not list:
            raise TypeError("list_rectangles must be a list")
        if type(list_squares) is not list:
            raise TypeError("list_squares must be a list")
        for inst in list_rectangles:
            if inst.__class__.__name__ != "Rectangle":
                raise TypeError("list_rectangles must be a list of instances"
                                " of Rectangle")
        for inst in list_squares:
            if inst.__class__.__name__ != "Square":
                raise TypeError("list_squares must be a list of instances"
                                " of Square")
        tpen = turtle.Turtle()
        tpen.penup()
        tpen.speed(1)
        tpen.color("white", "white")
        tscreen = tpen.getscreen()
        tscreen.bgcolor("black")
        for inst in [*list_rectangles, *list_squares]:
            tpen.setpos(inst.x, inst.y)
            tpen.pendown()
            tpen.forward(inst.width)
            tpen.left(90)
            tpen.forward(inst.height)
            tpen.left(90)
            tpen.forward(inst.width)
            tpen.left(90)
            tpen.forward(inst.height)
            tpen.left(90)
            tpen.penup()
