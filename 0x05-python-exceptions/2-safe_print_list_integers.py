#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0

    try:
        for i in range(x):
            print("{:d}".format(my_list[i]))
    except (ValueError, TypeError):
        pass
    else:
        length += 1
    print()

    return length
