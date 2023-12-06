i#!/usr/bin/python3
"""define dd"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Fcd Kdk"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dsdcds ds"""
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {km: getattr(self, km) for km in attrs if hasattr(self, km)}

        return self.__dict__
