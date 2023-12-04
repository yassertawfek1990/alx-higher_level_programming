#!/usr/bin/python3
"""Define las ald"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""
    def __init__(self, size):
        """self"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Methoeaare.'''
        return self.__size ** 2

    def __str__(self):
        '''Retur square.'''
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
