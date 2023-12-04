#!/usr/bin/python3
"""Defines ad"""


def inherits_from(obj, a_class):
    '''Dets if an ob.'''
    return isinstance(obj, a_class) and type(obj) != a_class
