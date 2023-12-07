#!/usr/bin/python3
def fizzbuzz():
    element = ""
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            element = "FizzBuzz"
        elif num % 3 == 0:
            element = "Fizz"
        elif num % 5 == 0:
            element = "Buzz"
        else:
            element = f"{num}"

        if num < 100:
            print("{} ".format(element), end="")
        else:
            print("{} ".format(element), end="")
