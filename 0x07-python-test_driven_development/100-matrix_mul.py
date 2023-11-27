#!/usr/bin/python3
"""Defiction."""


def matrix_mul(m_a, m_b):
    """Multiplatrices.

    Args:
        m_a (list of lists of ints/floats): The rix.
        m_b (list of lists of ints/floats): The atrix.
    Raises:
        TypeError: If of ints/floats.
        TypeError: If eipty.
        TypeError: If eient-sized rows.
        ValueError: If m_lied.
    Returns:
        A neon of m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(r, list) for r in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [n for r in m_a for n in r]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(e, int) or isinstance(e, float))
               for e in [n for r in m_b for n in r]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(r) == len(m_a[0]) for r in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(r) == len(m_b[0]) for r in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    q = []
    for w in range(len(m_b[0])):
        ne = []
        for z in range(len(m_b)):
            ne.append(m_b[z][w])
        q.append(ne)

    nm = []
    for r in m_a:
        nr = []
        for c in q:
            p = 0
            for d in range(len(q[0])):
                p += r[d] * c[d]
            ne.append(p)
        nm.append(nr)

    return nm
