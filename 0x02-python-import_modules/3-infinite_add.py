#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    argsLen = len(args)
    res = 0

    for i in range(argsLen):
        res += int(args[i])

    print(res)
