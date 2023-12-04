#!/usr/bin/python3
""" Define a"""


class Rectangle(BaseGeometry):
    """sdc sdd"""
    def __init__(self, width, height):
        """sdd  df"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
