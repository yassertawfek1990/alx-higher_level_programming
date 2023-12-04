#!/usr/bin/python3
"""Dahs jajd"""


class MyInt(int):
    """Gals fcsdc"""
    def __new__(cls, *args, **kwargs):
        """ferf"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """dsffv"""
        return int(self) != other

    def __ne__(self, other):
        """erffr ER"""
        return int(self) == other
