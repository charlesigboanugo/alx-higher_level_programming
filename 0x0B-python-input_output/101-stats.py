#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
    <status code> <file size>

    Each 10 lines and after a keyboard interruption (CTRL + C), prints

        Total file size: File size: <total size>
        All individual status codes with number greather than 0 in
        the format:
            <status code>: <number>

        where number is the sum of all previous (see input format above)
        Number of lines by status code:

        possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

        if a status code doesn’t appear, it doesn't print anything for that
        status code
"""
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
