#!/usr/bin/python3
""" """

import sys

status = {"200": 0, "301": 0, "400": 0, "401": 0,
          "403": 0, "404": 0, "405": 0, "500": 0}
logGrp = []
total_size = 0
logCount = 0
while True:
    try:
        singleLog = sys.stdin.readline()
        logGrp.append(singleLog)
        if (logCount + 1) % 10 == 0:
            for x, y in enumerate(logGrp):
                logarr = y.split(" ")
                status[logarr[-2]] += 1
                total_size += int((logarr[-1])[:-1])
            print(f"File size: {total_size}")
            for a in status.keys():
                if status[a] != 0:
                    print(f"{a}: {status[a]}")
            logGrp = []
        logCount += 1
    except KeyboardInterrupt:
        for x, y in enumerate(logGrp):
            logarr = y.split(" ")
            status[logarr[-2]] += 1
            total_size += int((logarr[-1])[:-1])
        print(f"File size: {total_size}")
        for a in status.keys():
            if status[a] != 0:
                print(f"{a}: {status[a]}")
        break
