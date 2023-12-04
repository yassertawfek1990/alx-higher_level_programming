#!/usr/bin/python3
"""Defines ad"""


def inherits_from(obj, a_class):
    """Return skad"""
    def inherits_from(obj, a_class):
        if isinstance(obj, a_class) and type(obj) != a_class:
            return True
        else:
            return False
