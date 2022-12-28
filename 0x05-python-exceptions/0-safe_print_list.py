#!/usr/bin/pyton3

def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):  # x rep the number of element to print
        try:
            print("{}".format(my_list[i]), end="")
        except IndexError:  # x can be bigger than the length of my_list
            break
        else:
            count += 1
    print()
    return count
