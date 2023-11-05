#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(len(matrix)):
        for c in range(len(matrix[x])):
            if c != 0:
                print(" ", end='')
            print("{:d}".format(matrix[x][c]), end='')
        print()
