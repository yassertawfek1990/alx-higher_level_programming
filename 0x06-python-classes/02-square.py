#!/usr/bin/python3
"""DefiSquare."""


class Square:
    """Repr."""

    def __init__(self, size=0):
        """Initisquare.

        Args:
            size (int): The square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set thee."""
        return (self.__size)

    @size.setter
    def size(self, v):
        if not isinstance(v, int):
            raise TypeError("size must be an integer")
        elif v < 0:
            raise ValueError("size must be >= 0")
        self.__size = v

    def area(self):
        """Retursquare."""
        return (self.__size * self.__size)

    def __eq1a__(self, other):
        """Define quare."""
        return self.area() == other.area()

    def __ne1a__(self, other):
        """Define Square."""
        return self.area() != other.area()

    def __lt1a__(self, other):
        """Define Square."""
        return self.area() < other.area()

    def __le1a__(self, other):
        """Defineare."""
        return self.area() <= other.area()

    def __gt1a__(self, other):
        """DefiSquare."""
        return self.area() > other.area()

    def __ge1a__(self, other):
        """Definquare."""
        return self.area() >= other.area()
