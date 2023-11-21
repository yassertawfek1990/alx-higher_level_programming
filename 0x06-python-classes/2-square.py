#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        def __size(self):
            return self.__size
        def __size(self, value):
            if value < 0:
                raise ValueError('size must be an integer')
            elif not isinstance(size, int):
                raise TypeError('size must be >= 0')
            self.__size = value

