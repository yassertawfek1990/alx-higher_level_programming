#!/usr/bin/python3
'''Moduse class.'''
from json import dumps, loads
import csv


class Base:
    '''A representatirarchy.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Cstuctor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifi longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unj ictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Sav ile.'''
        if list_objs is not None:
            list_objs = [e.to_dictionary() for e in list_objs]
        with open("{}.json".format(cls.__name__), "w") as fo:
            fo.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''Load onary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dictionary)
        return n

    @classmethod
    def load_from_file(cls):
        '''Loa ffs.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r") as fo:
            return [cls.create(**t) for t in cls.from_json_string(fo.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Sav file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[e.id, e.width, e.height, e.x, e.y]
                             for e in list_objs]
            else:
                list_objs = [[e.id, e.size, e.x, e.y] for e in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='') as fo:
            w = csv.writer(fo)
            w.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Lo ile.'''
        from models.rectangle import Rectangle
        from models.square import Square
        m = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='') as fo:
            q = csv.reader(fo)
            for r in q:
                r = [int(c) for c in r]
                if cls is Rectangle:
                    k = {"id": r[0], "width": r[1], "height": r[2],
                         "x": r[3], "y": r[4]}
                else:
                    k = {"id": r[0], "size": r[1], "x": r[2], "y": r[3]}
                m.append(cls.create(**k))
        return m

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for v in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((v.x + t.pos()[0], v.y - t.pos()[1]))
            t.pensize(10)
            t.forward(v.width)
            t.left(90)
            t.forward(v.height)
            t.left(90)
            t.forward(v.width)
            t.left(90)
            t.forward(v.height)
            t.left(90)
            t.end_fill()
        time.sleep(5)
