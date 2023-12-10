#!/usr/bin/python3
"""define dd"""
import json


class Base:
    """sfdsfsdf"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is not None:
            list_objs = [x.to_dictionary() for x in list_objs]
        with open("{}.json".format(cls.__name__), "w") as h:
            h.write(cls.to_json_string(list_objs))
    
    @staticmethod
    def from_json_string(json_string):
        """sdv dvs"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """fvdfv gfggd"""
        from models.square import Square
        from models.rectangle import Rectangle
        if cls.__name__ is Square:
            n = Squar(1)
        elif cls.__name__ is Rectangle:
            n = Rectangle(1, 1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        """sdf sdd"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(f, "r") as x:
            return (cls.create(**m) for m in cls.from_json_string(x.read()))

