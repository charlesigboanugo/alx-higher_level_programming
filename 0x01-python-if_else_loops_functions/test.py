#!/usr/bin/python3
def uppercase(str):
    for s in str:
        test = ord(s) >= ord('a') and ord(s) <= ord('z')
        print("{}".format(chr(ord(s) - 32) if test else s), end="")
    print()
