#!/usr/bin/python3
'''Modu foss.'''
from models.base import Base


class Rectangle(Base):
    """Rent angle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a nd"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Setet tngle."""
        return self.__width

    @width.setter
    def width(self, b):
        if type(b) != int:
            raise TypeError("width must be an integer")
        if b <= 0:
            raise ValueError("width must be > 0")
        self.__width = b

    @property
    def height(self):
        """St hRectangle."""
        return self.__height

    @height.setter
    def height(self, b):
        if type(b) != int:
            raise TypeError("height must be an integer")
        if b <= 0:
            raise ValueError("height must be > 0")
        self.__height = b

    @property
    def x(self):
        """Se theectangle."""
        return self.__x

    @x.setter
    def x(self, b):
        if type(b) != int:
            raise TypeError("x must be an integer")
        if b < 0:
            raise ValueError("x must be >= 0")
        self.__x = b

    @property
    def y(self):
        """Sehe ctangle."""
        return self.__y

    @y.setter
    def y(self, b):
        if type(b) != int:
            raise TypeError("y must be an integer")
        if b < 0:
            raise ValueError("y must be >= 0")
        self.__y = b
