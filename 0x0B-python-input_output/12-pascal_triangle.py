#!/usr/bin/python3
"""Defines a function that returns a list of lists containing
N sized pascal's triangle"""


def pascal_triangle(n):
    """Returns a pascal's triangle of size n as a list of lists"""
    arr = []
    for x in range(n):
        sub = [1]
        if x != 0:
            for y in range(len(arr[x - 1]) - 1):
                sub.append(arr[x - 1][y] + arr[x - 1][y + 1])
            sub.append(1)
        arr.append(sub)
    return arr
