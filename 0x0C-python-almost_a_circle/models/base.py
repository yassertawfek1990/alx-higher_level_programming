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
        '''Jsoes longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        '''Unjsdict ionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Savn ct tile.'''
        if list_objs is not None:
            list_objs = v.to_dictionary() for v in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as fo:
            fo.write(cls.to_json_string(list_objs))

    @classmethod
    def create(cls, **dictionary):
        '''tance froionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            n = Rectangle(1, 1)
        elif cls is Square:
            n = Square(1)
        else:
            n = None
        n.update(**dic)
        return n

    @classmethod
    def load_from_file(cls):
        '''Loas fies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as fo:
            return [cls.create(**v) for v in cls.from_json_string(fo.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Sav v file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                l = [[v.id, v.width, v.height, v.x, v.y] for v in list_objs]
            else:
                l = [[v.id, v.size, v.x, v.y] for v in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='', encoding='utf-8') as fo:
            w = csv.writer(fo)
            w.writerows(l)

    @classmethod
    def load_from_file_csv(cls):
        '''Loadsf ile.'''
        from models.rectangle import Rectangle
        from models.square import Square
        w = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='', encoding='utf-8') as fo:
            der = csv.reader(fo)
            for r in der:
                r = [int(h) for h in r]
                if cls is Rectangle:
                    k = {"id": r[0], "width": r[1], "height": r[2], "x": r[3], "y": r[4]}
                else:
                    k = {"id": r[0], "size": r[1], "x": r[2], "y": r[3]}
                w.append(cls.create(**k))
        return w

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
