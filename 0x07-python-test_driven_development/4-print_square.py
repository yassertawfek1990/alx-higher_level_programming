#!/usr/bin/python3
"""Definetion."""


def print_square(size):
    """Printaracter.

    Args:
        size (int): The huare.
    Raises:
        TypeError: eger.
        ValueError: s < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for c in range(size)]
        print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
