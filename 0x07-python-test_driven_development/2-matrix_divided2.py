#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix by a number"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div and returns a new matrix"""
    if type(matrix) is not list:
        raise TypeError("""matrix must be a matrix (list of lists)
        of integers/floats""")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div != div or div == -float("inf") or div == float("inf"):
        div = 2
    matrix_len = len(matrix)
    if matrix_len != 0 and type(matrix[0]) is list:
        row_len = len(matrix[0])
    for x in range(matrix_len):
        if type(matrix[x]) is not list:
            raise TypeError("""matrix must be a matrix (list of lists)
            of integers/floats""")
        if len(matrix[x]) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for y in range(row_len):
            if type(matrix[x][y]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) \
                                of integers/floats")
            if matrix[x][y] != matrix[x][y] or matrix[x][y] == -float("inf") \
                    or matrix[x][y] == float("inf"):
                        matrix[x][y] = 2
            matrix[x][y] = round(matrix[x][y] / div, 2)
    return matrix
