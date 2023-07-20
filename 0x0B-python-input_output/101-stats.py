#!/usr/bin/python3
import sys


codes = {}
totalsize = 0
linesread = 0
try:
    for line in sys.stdin:
        line = line.split(" ")
        if line[-2] in codes:
            codes[line[-2]] += 1
        elif line[-2] in ["200", "301", "400", "401",
                          "403", "404", "405", "500"]:
            codes[line[-2]] = 1
        else:
            continue
        totalsize += int(line[-1])
        linesread += 1
        if linesread % 10 == 0:
            print("File size:", totalsize)
            for code in sorted(list(codes)):
                print("{}: {}".format(code, codes[code]))
finally:
    print("File size:", totalsize)
    for code in sorted(list(codes)):
        print("{}: {}".format(code, codes[code]))
