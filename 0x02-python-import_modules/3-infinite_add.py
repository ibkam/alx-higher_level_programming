#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) < 2):
        print("0")
    elif (len(argv) == 2):
        print(argv[1])
    else:
        # duplicate the loop in iterate through argument list to convert int
        dup = [int(argv[i]) for i in range(1, len(argv))]
        # sum is the iteration of list of argument
        Sum = sum(dup)
        print(Sum)
