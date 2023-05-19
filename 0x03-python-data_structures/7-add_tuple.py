#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == None or tuple_b == None:
        return
    x = 0
    if len(tuple_a) != 0 and tuple_a[0] != None:
        x += tuple_a[0]
    if len(tuple_b) != 0 and tuple_b[0] != None:
        x += tuple_b[0]
    y = 0
    if len(tuple_a) > 1 and tuple_a[1] != None:
        y += tuple_a[1]
    if len(tuple_b) > 1 and tuple_b[1] != None:
        y += tuple_b[1]
    return x, y

