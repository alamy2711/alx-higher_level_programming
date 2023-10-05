#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    argsLen = len(args)

    if argsLen == 0:
        print("0 arguments.")
    elif argsLen == 1:
        print("1 argument:")
    elif argsLen > 1:
        print(f"{argsLen} arguments:")

    for i in range(argsLen):
        print(f"{i + 1}: {args[i]}")
