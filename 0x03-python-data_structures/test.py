#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return
    for row in matrix:
        if row is not None:
            for x in range(0, len(row)):
                print("{:d}".format(row[x]), end='')
                if x != len(row) - 1:
                    print(" ", end='')
        print()
