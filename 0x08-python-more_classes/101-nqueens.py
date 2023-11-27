#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines  an NxN chessboard.

Example:
    $ ./101-nqueens.py o 4.

Attributes:
    board (list): A list ofsboard.
    solutions (list): A lisions.

Solutions are repr
"""
import sys


def ba(n):
    """I 0's."""
    l = []
    [l.append([]) for q in range(n)]
    [s.append(' ') for q in range(n) for s in l]
    return (l)

def bd(l):
    """Returard."""
    if isinstance(l, list):
        return list(map(bd, l))
    return (l)


def gs(l):
    """Returssboard."""
    sol = []
    for z in range(len(l)):
        for a in range(len(l)):
            if l[z][a] == "Q":
                sol.append([z, a])
                break
    return (sol)

def xo(l, s, c):
    """X ouard.

    All

    Args:
        board (list): Tssboard.
        row (int): The  played.
        col (int): The colayed.
    """
    for z in range(c + 1, len(l)):
        l[s][z] = "x"
    for z in range(c - 1, -1, -1):
        l[s][z] = "x"
    for w in range(s + 1, len(l)):
        l[w][c] = "x"
    for w in range(s - 1, -1, -1):
        l[w][c] = "x"
    z = c + 1
    for w in range(s + 1, len(l)):
        if z >= len(l):
            break
        l[w][z] = "x"
        z += 1
    z = c - 1
    for w in range(s - 1, -1, -1):
        if z < 0:
            break
        l[w][z]
        z -= 1
    z = c + 1
    for w in range(s - 1, -1, -1):
        if z >= len(l):
            break
        l[w][z] = "x"
        z += 1
    z = c - 1
    for w in range(s + 1, len(l)):
        if z < 0:
            break
        l[w][z] = "x"
        z -= 1

def rec(l, s, qu, sol):
    """Recursive.

    Args:
        board (list): Theboard.
        row (int): Tg row.
        queens (int): Thaced queens.
        solutions (list): A  of solutions.
    Returns:
        sol
    """
    if qu == len(l):
        sol.append(gs(l))
        return (sol)

    for z in range(len(l)):
        if l[s][z] == " ":
            t = bd(l)
            t[s][z] = "Q"
            xo(t, s, z)
            sol = rec(t, s + 1, qu + 1, sol)
    return (sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    l = ba(int(sys.argv[1]))
    sol = rec(l, 0, 0, [])
    for d in sol:
        print(d)
