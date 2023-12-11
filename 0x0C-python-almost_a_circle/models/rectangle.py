#!/usr/bin/python3
'''Modu foss.'''
from models.base import Base


class Rectangle(Base):
    '''A Recss.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Cotor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Wid otangle.'''
        return self.__width

    @width.setter
    def width(self, v):
        self.validate_integer("width", v, False)
        self.__width = v

    @property
    def height(self):
        '''Hei ectangle.'''
        return self.__height

    @height.setter
    def height(self, v):
        self.validate_integer("height", v, False)
        self.__height = v

    @property
    def x(self):
        '''x tangle.'''
        return self.__x

    @x.setter
    def x(self, v):
        self.validate_integer("x", v)
        self.__x = v

    @property
    def y(self):
        '''yof tngle.'''
        return self.__y

    @y.setter
    def y(self, v):
        self.validate_integer("y", v)
        self.__y = v
