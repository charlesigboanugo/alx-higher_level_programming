#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    ac = len(argv) - 1
    print("{} argument{}".format(ac, "s" if ac != 1 else ""), end="")
    print("{}".format(":" if ac else "."))
    for ind, arg in enumerate(argv[1:], 1):
        print("{}: {}".format(ind, arg))
