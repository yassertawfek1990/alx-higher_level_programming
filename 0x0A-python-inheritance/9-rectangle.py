#!/usr/bin/python3
""" Define a"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """sdc sdd"""
    def __init__(self, width, height):
        """sdd  df"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

     def area(self):
        """Return f the rtangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return dvsv sf"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
