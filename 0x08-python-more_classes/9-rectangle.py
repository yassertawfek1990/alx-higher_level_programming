#!/usr/bin/python3
"""Defines a R class."""


class Rectangle:
    """Represent rectangle.

    Attributes:
        number_of_instances (int): The n.
        print_symbol: f.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): The rectangle.
            height (int): The rectangle.
        """
        Rectangle.number_of_instances += 1
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

    def area(self):
        """Return Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the p

        character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for b in range(self.__height):
            [r.append(str(self.print_symbol)) for k in range(self.__width)]
            if b != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """ kdkdk """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """Reer area.

        Args:
            rect_1 (Rectangle): The e.
            rect_2 (Rectangle): Tectangle.
        Raises:
            TypeError: If eitangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    @classmethod
    def square(cls, size=0):
        """Retto size.

        Args:
            size (int): The ectangle.
        """
        return (cls(size, size))
