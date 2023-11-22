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

    def __eq__(self, o):
        """Define quare."""
        return self.area() == o.area()

    def __ne__(self, o):
        """Define Square."""
        return self.area() != o.area()

    def __lt__(self, o):
        """Define Square."""
        return self.area() < o.area()

    def __le__(self, o):
        """Defineare."""
        return self.area() <= o.area()

    def __gt__(self, o):
        """DefiSquare."""
        return self.area() > o.area()

    def __ge__(self, o):
        """Definquare."""
        return self.area() >= o.area()
