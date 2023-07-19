#!/usr/bin/python3


def pas(n):
    arr = []
    for x in range(n):
        sub = [1]
        if x != 0:
            for y in range(len(arr[x - 1]) - 1):
                sub.append(arr[x - 1][y] + arr[x - 1][y + 1])
            sub.append(1)
        arr.append(sub)
    return arr
