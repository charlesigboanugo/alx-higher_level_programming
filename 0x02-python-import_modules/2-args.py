#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    av = argv[1:]
    avlen = len(av)
    print("{} argument{}".format(avlen, "s" if avlen != 1 else ""), end="")
    print("{}".format(":" if avlen else "."))
    for i, v in enumerate(av):
        print("{}: {}".format(i + 1, v))
