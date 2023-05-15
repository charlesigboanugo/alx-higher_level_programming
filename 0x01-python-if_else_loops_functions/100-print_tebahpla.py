#!/usr/bin/python3
for c in range(122, 96, -1):
    print("{}".format(chr(c - 32) if c % 2 else chr(c)), end="")
