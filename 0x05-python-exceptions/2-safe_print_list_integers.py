#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        length = 0

        for i in range(x):
            print("{:d}".format(my_list[i]))
            length += 1
    except (ValueError, TypeError, SyntaxError):
        pass
    print()

    return length
