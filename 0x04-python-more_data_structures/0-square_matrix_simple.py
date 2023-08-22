#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    updated_matrix = matrix.copy()

    for n in range(len(matrix)):
        updated_matrix[n] = list(map(lambda x: x**2, matrix[n]))

    return (updated_matrix)
