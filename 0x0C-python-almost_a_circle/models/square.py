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
