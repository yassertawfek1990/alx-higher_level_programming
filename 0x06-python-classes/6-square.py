#!/usr/bin/python3
"""Define a claasaaaaaaaaaaaaaaaaaaass Square."""


class Square:
    """Reprasssssssssssssssssssesent aasas square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializeasaasacsa asac nassaew square.

        Args:
            size (int): The size of asasthe nassaasew square.
            position (int, int): The posasasassaition of the neaasasw square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the currasdasent sizeasdasdasdas of the square."""
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
        """Get/set the curasdasdasrent pasdasdasdosition of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(v, int) for v in value) or
                not all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the cursdaasdasrent arasdsasea of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the squarasdassade with the sadds# asdasdcharacter."""
        if self.__size == 0:
            print("")
            return

        [print("") for wrwr in range(0, self.__position[1])]
        for e in range(0, self.__size):
            [print(" ", end="") for r in range(0, self.__position[0])]
            [print("#", end="") for t in range(0, self.__size)]
            print("")
