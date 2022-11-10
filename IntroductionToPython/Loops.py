# While loop example 1
from random import randint
name = "Iqra"

while name != "Iqra":
    name = input("Name: ")

print("You are free!")

# While loop example 2
like_rice = True

if not like_rice:
    print("You hate rice")
else:
    print("You like rice")

# While loop example 3
while True:
    print("Hello")

print("Goodbye.")

# While loop example 4
while True:
    num1 = int(input("Give me a number: "))
    num2 = int(input("Give me another number: "))

    ans = num1 * num2

    print("\033[32m" + str(num1) + " * " +
          str(num2) + " = " + str(ans) + "\033[0m\n")

# FOR AND WHILE LOOP EXAMPLE: Both execute the same result just different words (if, while):
for x in range(5):
    print(x)

count = 0
while count < 5:
    print(count)
    count == 1

# While loop
num = randint(1, 5)
guess = input("Guess a number between 1 and 51: ")
lives = 2

while int(guess) != num and lives > 0:
    lives -= 1
    print("try again")
    guess = input("Guess a number between 1 and 51: ")

if guess == num:
    print("You guessed right!")
else:
    print("You ran out of tries :(")
