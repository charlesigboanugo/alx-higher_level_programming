#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a is None or tuple_b is None:
        return
    x = 0
    if len(tuple_a) != 0 and tuple_a[0] is not None:
        x += tuple_a[0]
    if len(tuple_b) != 0 and tuple_b[0] is not None:
        x += tuple_b[0]
    y = 0
    if len(tuple_a) > 1 and tuple_a[1] is not None:
        y += tuple_a[1]
    if len(tuple_b) > 1 and tuple_b[1] is not None:
        y += tuple_b[1]
    return x, y
