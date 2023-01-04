#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if len(argv) - 1 != 3:
        print("usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        # converting input parameters to intergers
        a = int(argv[1])
        b = int(argv[3])

        # handling  basic operators
        if argv[2] == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif argv[2] == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif argv[2] == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif argv[2] == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
