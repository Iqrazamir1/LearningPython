# 1. Strings are character
from random import randint
name = " Iqra"
username = "Iqra_zamir22"
today_date = "20/10/2021"

# 2. Integers are whole numbers 
house_number = 76
age = 87
goals_against_united = 3

# 3. Float is a decimal number
shoe_size = 9.5
bank_balance = -7000.25

# 4. Boolean (Binary - True or False / Yes or  No) 
is_light_on = False

# Notes: Casting is converting one data type to another eg. strings to integer(int).
# covert to string - str()
# convert to integer - int()
# convert to float - float()

# Example one of making a dice
input("Press [Enter] to roll")
dice = str(randint(1, 6))
print("You rolled a " + dice)

input("Press [Enter] to roll again")
dice = str(randint(1, 6))
print("You rolled a " + dice)

# Example two of making a dice
guess = input(("pick a number between 1 and 6:"))

input("Press [Enter] to roll")
dice = str(randint(1, 6))
print("You rolled a " + dice)

input("Press [Enter] to roll again")
dice = str(randint(1, 6))
print("You rolled a " + dice)

if guess == dice:
    print("you were right!")
else:
    print("You were wrong")
