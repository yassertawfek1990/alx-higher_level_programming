#!/usr/bin/python3
"""define dd"""


def Square(Rectangle):
    """Square Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        Super().__init__(size, size, x, y, id)

     def __str__(self):
        """Re and str() rep"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.getter
    def size(self, v):
        self.width = v
        self.height = v

     def _update_(self,id=None,size=None,y=None,x=None):
        """Update"""
        if id != None:
            self.id = id
        if width != None:
            self.size = size
        if x != None:
            self.x = x
        if y != None:
            self.y = y

    def update(self, *args, **kwargs):
        """asd fdf"""
        if args:
            self._update_(self, *args)
        elif kwargs:
            self._update_(self, **kwargs)

    def to_dictionary(self):
        """sdd fsds"""
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
