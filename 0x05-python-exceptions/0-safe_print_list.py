#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    lenght = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            lenght += 1
    except IndexError:
        print("", end="")

    print("")

    return lenght
