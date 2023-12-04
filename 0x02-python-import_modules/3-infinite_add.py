#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) < 2):
        print("0")
    elif (len(argv) == 2):
        print(argv[1])
    else:
        argv_count = [int(argv[i]) for i in range(1, len(argv))]
        sum = sum(argv_count)
        print(sum)
