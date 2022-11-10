# Operators:
# Adding +
# Subtraction =
# Multiolication *
# Real division /
# interger division // - (normal division without the float - decimal)
# Modulo (MOD) % (only works with whole numbers)
# Powers **

import random
from math import ceil
from random import randint
number = 10
# Divide the number by 5
number = number / 5
# Round up to nearest integeer
number = ceil(number)
# Multipiply new number by 5
number = number * 5
print(number)

def rounf_to_next5(n):
    div = n / 5
    rounded = ceil(div)
    answer = rounded * 5
    return n

# Rounding numbers example
number = 6.7672
rounded = round(number)
print(rounded)

# COMPARING THE POSITIVES OF BOTH CODES
number = randint(1, 5)
print(number)
# Norrows down the load rather than having unnessaccary things (allow programms to run faster).
whole_number = random.randint(1, 5)
decimal_number = random.uniform(1, 5)
print(whole_number, decimal_number)

# Modulo
total = 567
sweets = total // 4
left = total % 4
print(sweets + left)

# Modulo example
number = 1  # can change this number
answer = number % 3
print(answer)

# Modulo example
number = randint(0, 100)
if number % 2 == 0:
    print(str(number) + "is even")
if number % 2 == 1:
    print(str(number) + "is odd")

# Challenge
def int_input(prompt):
    while True:
        try:
            response = int(input(prompt))
            return response
        except ValueError:
            print("\033[0;31;0m"+"Please enter a valid number"+"\033[0;0;0m")

num = int_input("Enter the number:")

def recur_reverse(num):
    return str(num)[::-1]

print(recur_reverse(num))
