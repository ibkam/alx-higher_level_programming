#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) < 2):
        print("0")
    elif (len(argv) == 2):
        print(argv[1])
    else:
        # iterate through argument list
        argv_count = [int(argv[i]) for i in range(1, len(argv))]
        # sum the iterate list
        Sum = sum(argv_count)
        print(Sum)
