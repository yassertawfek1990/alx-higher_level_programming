i#!/usr/bin/python3
"""define dd"""


class Student:
    """Represeent."""

    def __init__(self, first_name, last_name, age):
        """Initialize a"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary represe"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
