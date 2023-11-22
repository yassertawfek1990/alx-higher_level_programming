#!/usr/bin/python3
"""Definere."""


class Square:
    """Repreuare."""

    def __init__(self, size=0, position=(0, 0)):
        """Initi re.

        Args:
            size (int): T square.
            position (int, int): Tnew square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set thsquare."""
        return (self.__size)

    @size.setter
    def size(self, v):
        if not isinstance(v, int):
            raise TypeError("size must be an integer")
        elif v < 0:
            raise ValueError("size must be >= 0")
        self.__size = v

    @property
    def position(self):
        """Get/set t quare."""
        return (self.__position)

    @position.setter
    def position(self, v):
        if (not isinstance(v, tuple) or
                len(v) != 2 or
                not all(isinstance(x, int) for x in v) or
                not all(x >= 0 for x in v)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = v

    def area(self):
        """Retuthe square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print tter."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for z in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for s in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define thuare."""
        if self.__size != 0:
            [print("") for x in range(0, self.__position[1])]
        for z in range(0, self.__size):
            [print(" ", end="") for a in range(0, self.__position[0])]
            [print("#", end="") for s in range(0, self.__size)]
            if z != self.__size - 1:
                print("")
        return ("")
