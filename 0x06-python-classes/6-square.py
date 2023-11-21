#!/usr/bin/python3
"""Define sddddddddddddddddddddddda class Square."""


class Square:
    """Represdssssssssssssssssssssssent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initiawwwdsssssssssssssssssssssssw Square.

        Args:
            size (int): Thesaddddddddddseesquare.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get/set the current size of tsddddddddddhedvsvsdv square."""
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
        """Get/set tsddddddddddddddddddhe current size of thedvsvsdv square."""
        return (self.__position)

    @size.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(f, int) for f in value) or
                not all(f >= 0 for f in value)):
            raise TypeError("sposition must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the currensddddddsdt area of the square.sdvsvsvsv"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the ssdddddddddddquare with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for q in range(0, self.__position[1])]
        for w in range(0, self.__size):
            [print(" ", end="") for e in range(0, self.__position[0])]
            [print("#", end="") for r in range(0, self.__size)]
            print("")
