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
        if not isinstance(v, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        return self.__height

    @height.getter
    def height(self, v):
        if not isinstance(v, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = v

    @property
    def y(self):
        return self.__y

    @y.getter
    def y(self, v):
        if not isinstance(v, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = v

    @property
    def x(self):
        return self.__x

    @x.getter
    def x(self, v):
        if not isinstance(v, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("y must be >= 0")
        self.__x = v

