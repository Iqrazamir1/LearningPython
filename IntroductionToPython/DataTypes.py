from random import randint
# Python has the following data types built-in by default, in these categories:

# Text Type - str (can only concatinate string)
dataTypeString = str("Hello world!")

# Numeric Type - int (whole numbers), float (decimal numbers), complex
dataTypeInt = int(20)
dataTypeFloat = float(20.5)
dataTypeComplex = complex(1j)

# Binary Types - bytes, bytearray, memoryview
dataTypeBytes = bytes(5)
dataTypeBytearray = bytearray(5)
dataTypeMemoryview = memoryview(bytes(5))

# Boolean Type - bool (Binary - True or False / Yes or  No / On or Off)
dataTypeBoolean = bool(5)

# Sequence Types - list, tuple, range
listExample = list(("Apple", "Banana", "Cherry"))
tupleExample = tuple(("Apple", "Banana", "Cherry"))
rangeExample= range(6)

# Mapping Type - dict
dictionaryExample = dict (
    name = "Iqra",
    age = 21
)

# Set Types - set, frozenset
setExample = set(("Apple", "Banana", "Cherry"))
frozensetExample = frozenset(("Apple", "Banana", "Cherry"))

# EXAMPLE 1. Making a dice
input("Press [Enter] to roll")
dice = str(randint(1, 6))
print("You rolled a " + dice)

# EXAMPLE 2. Making a dice
guess = input(("pick a number between 1 and 6:"))

input("Press [Enter] to roll")
dice = str(randint(1, 6))
print("Your number is " + dice)

if guess == dice:
    print("you were right!")
else:
    print("You were wrong")
