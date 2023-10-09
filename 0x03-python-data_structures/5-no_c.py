#!/usr/bin/env python3
def no_c(my_string):
    newString = ""
    for i in range(len(my_string)):
        if my_string[i] not in "Cc":
            newString += my_string[i]
    return newString
