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
