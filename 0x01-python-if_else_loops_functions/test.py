#!/usr/bin/python3
for c in range(122, 96, -1):
    letter = chr(c)
    if c % 2 == 1:
        letter = chr(c - 32)
    print("{}".format(letter), end="")
