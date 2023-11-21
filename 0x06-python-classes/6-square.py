#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initiawwww Square.

        Args:
            size (int): Theeesquare.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of thedvsvsdv square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get/set the current size of thedvsvsdv square."""
        return (self.__position)

    @size.setter
    def position(self, value):
        if (not isinstance(value, tuple)) or (value[1] < 0) or (value[0] < 0) or len(value) != 2 or (not isinstance(value[1], tuple)) or (not isinstance(value[0], int)):
            raise TypeError("sposition must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square.sdvsvsvsv"""
        return (self.__size * self.__size)

    def my_print(self):
        """Return the current area of the square.sdvsvsvsv"""
        if self.__size == 0:
            print("")
        else:
            for s in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for m in range(self.__size):
                    print("#", end="")
                print("")
