#!/usr/bin/python3
"""define dd"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Fcd Kdk"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dsdcds ds"""
        return self.__dict__
