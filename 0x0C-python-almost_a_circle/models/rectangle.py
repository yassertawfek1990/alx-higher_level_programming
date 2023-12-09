#!/usr/bin/python3
"""define dd"""
from models.Base import Base


class Rectangle(Base):
    """csdcdv"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.getter
    def width(self, v):
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.getter
    def height(self, v):
        self.__height = v

    @property
    def y(self):
        return self.__y

    @y.getter
    def y(self, v):
        self.__y = v

    @property
    def x(self):
        return self.__x

    @x.getter
    def x(self, v):
        self.__x = v

