#!/usr/bin/python3
"""Defines a R class."""


class Rectangle:
    """Represent rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): The rectangle.
            height (int): The rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set tangle."""
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
        """Get/set ectangle."""
        return self.__height

    @height.setter
    def height(self, v):
        if not isinstance(v, int):
            raise TypeError("height must be an integer")
        if v < 0:
            raise ValueError("height must be >= 0")
        self.__height = v
