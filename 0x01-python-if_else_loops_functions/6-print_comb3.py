#!/usr/bin/python3
for n in range(0, 10):
    for m in range(n + 1, 10):
        print("{}{}".format(n, m), end="")
        if n != 8 and n != 9:
            print(", ", end="")
print()
