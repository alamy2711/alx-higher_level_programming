#!/usr/bin/python3

import sys

dict_status = {}
total_size = 0
total_count = 0

for line in sys.stdin:
    split = line.split()
    status = split[-2]
    total_size += int(split[-1])

    if status in dict_status:
        dict_status[status] += 1
    else:
        dict_status[status] = 1

    total_count += 1

    if total_count == 10:
        sorted_keys = sorted(dict_status.keys())
        print("File size:", total_size)

        for key in sorted_keys:
            print("{}: {}".format(key, dict_status[key]))

        total_count = 0
