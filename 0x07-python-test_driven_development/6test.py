#!/usr/bin/python3
"""Defines a function that multipies two matrices"""


def matrix_mul(m_a, m_b):
    """Does the dot multiplication of matrix m_a and matrix ma_b""" 
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for row in m_a:
        if type(row) is not list:
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if type(row) is not list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    arow_size = len(m_a[0])
    brow_size = len(m_b[0])
    for row in m_a:
        if len(row) != arow_size:
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != brow_size:
            raise TypeError("each row of m_b must be of the same size")
    if arow_size != len(m_b):
            raise ValueError("m_a and m_b can't be multiplied")
    row = []
    for x in range(len(m_a)):
        col = []
        for y in range(brow_size):
            sumpro = 0
            for z in range(arow_size):
                sumpro += m_a[x][z] * m_b[z][y]
            col.append(sumpro)
        row.append(col)
    return row
