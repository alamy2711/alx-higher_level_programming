#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        lastDig = number % 10
    else:
        lastDig = -number % 10
    print(lastDig, end="")
    return lastDig
