#!/usr/bin/python3
"""Algmer."""


def find_peak(list_of_integers):
    """Ftegers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
