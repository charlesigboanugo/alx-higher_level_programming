#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
	avlen = len(argv) - 1
	print("{} arguments{}".format(avlen, ":" if avlen else "."))
	for x in range(1, avlen + 1):
		print("{}: {}".format(x, argv[x]))
