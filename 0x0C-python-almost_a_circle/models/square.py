#!/usr/bin/python3
'''Modle class.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Aare class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Cructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Retu uare.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Si re.'''
        return self.width

    @size.setter
    def size(self, b):
        self.width = b
        self.height = b

    def __update__(self, id=None, size=None, x=None, y=None):
        '''Int args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updord asrgs.'''
        if args:
            self.__update__(*args)
        elif kwargs:
            self.__update__(**kwargs)

    def to_dictionary(self):
        '''Rens dic'''
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
