#!/usr/bin/python3
"""define dd"""


def Square(Rectangle):
    """Square Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        Super().__init__(size, size, x, y, id)

     def __str__(self):
        """Re and str() rep"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
