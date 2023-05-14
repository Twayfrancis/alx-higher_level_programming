#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for col in row:
            print("{0:2d}".format(col), end="")
        print()
