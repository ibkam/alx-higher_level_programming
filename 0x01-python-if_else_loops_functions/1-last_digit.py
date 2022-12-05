#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = number
if num < 0:
    last_digit = (num % 10) * -1
else:
    last_digit = (num % 10)

if last_digit > 5:
    print(f"last digit of {num} is {last_digit} and is greater than 5")
elif last_digit < 6 or last_digit != 0:
    print(f"last digit of {num} is {last_digit} and is less than 6 and not 0")
else:
    print(f"last digit of {num} is {0} and is 0")
