#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        return
    for row in matrix:
        if row is not None:
            for x in range(0, len(row)):
                print("{:d}".format(row[x]), end='')
                if x is not len(row) - 1:
                    print(" ", end='')
        print()
print_matrix_integer([[1, 2, 3], None, [7, None, 9]])
