#!/usr/bin/python3
import math


class MagicClass:
    """Reprercle."""

    def __init__(self, radius=0):
        """InClass.

        Arg:
            radiusncClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Ret"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """R"""
        return (2 * math.pi * self.__radius)
