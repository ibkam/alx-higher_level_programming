#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in ranfe(x):
        try:
            print("{}".format(my_list[i]), end="")
        expect IndexError:
            break
        else:
            count += 1
    print()
    return count
