#!/usr/bin/python3
def islower(c):
    if ord(c) in range(65, 91):
        return False
    if ord(c) in range(97, 123):
        return True
