#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix_copy = [el.copy() for el in matrix]
    return list(map(lambda r: list(map(lambda c: c ** 2, r)), matrix_copy))
