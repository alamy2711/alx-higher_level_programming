#!/usr/bin/python3
j = 1
for i in reversed(range(97, 123)):
    if j % 2 != 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
    j += 1
