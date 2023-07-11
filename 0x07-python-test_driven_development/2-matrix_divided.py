#!/usr/bin/python3
"""Module that contains a function to divide a matrix by a scalar"""


def matrix_divided(matrix, div):
    """Divides all elements in matrix by div and returns a new matrix"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    rowlen = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if len(row) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            new_row.append(round(float(x / div), 2))
        new_matrix.append(new_row)
    return new_matrix
