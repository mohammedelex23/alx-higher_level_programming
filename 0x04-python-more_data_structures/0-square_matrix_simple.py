#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy_matrix = [item.copy() for item in matrix]

    for row in range(0, len(copy_matrix)):
        for col in range(0, len(copy_matrix[row])):
            copy_matrix[row][col] = copy_matrix[row][col] ** 2
    return copy_matrix
