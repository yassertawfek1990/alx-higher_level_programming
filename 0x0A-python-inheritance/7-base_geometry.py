#!/usr/bin/python3
"""Define ska"""


class BaseGeometry:
    """ddaddsc f"""
    def area(self):
        """"dd"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ jasdjajdc sdsd"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
