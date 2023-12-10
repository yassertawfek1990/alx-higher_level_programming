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


