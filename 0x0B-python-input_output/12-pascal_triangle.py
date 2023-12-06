#!/usr/bin/python3
"""define dd"""


def pascal_triangle(n):
    """Represent Pasc"""
    if n <= 0:
        return []
    tr = [[1]]
    while len(tr) != n:
        ri = tr[-1]
        t = [1]
        for x in range(len(ri) - 1):
            t.append(ri[x] + ri[x + 1])
        t.append(1)
        tr.append(t)
    return tr
