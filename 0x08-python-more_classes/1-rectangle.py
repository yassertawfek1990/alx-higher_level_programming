#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """a rectangle."""
    def __init__(self, width=0, height=0):
         """ new Rectangle.

        Args:
            width (int): rectangle.
            height (int): The heigh rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/srectangle."""
        return self.__width

    @width.setter
    def width(self, v):
        if not isinstance(v, int):
            raise TypeError("width must be an integer")
        if v < 0:
            raise ValueError("width must be >= 0")
        self.__width = v

    @property
    def height(self):
        """Get/se rectangle."""
        return self.__height

    @height.setter
    def height(self, v):
        if not isinstance(v, int):
            raise TypeError("height must be an integer")
        if v < 0:
            raise ValueError("height must be >= 0")
        self.__height = v
