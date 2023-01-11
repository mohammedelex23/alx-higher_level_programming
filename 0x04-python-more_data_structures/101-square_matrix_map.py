#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix_copy = [el.copy() for el in matrix]
    return list(map(lambda row: list(map(lambda col: col ** 2, row)), matrix_copy))
