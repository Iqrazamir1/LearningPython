# NESTED CONDITION: If statement within a if statement 

# ONE STEP SYSTEM: both username and password have to be correct for access.
username = input("username: ")
password = input("password: ")

if username == "Iqra" and password == "Orange":
    print("Welcome Iqra")
elif username == "Hiree" and password == "Red":
    print("Welcome Hiree")
else:
    print("Access denied!")

# TWO STEP SYSTEM: Only allows acces when both username and password are correct (if any information 
# is wrong you will recive error message - More Secure)
username = input("username: ")

if username == "Ibby":
    password = input("password: ")
    if password == "fun":
        print("Welcome Ibby")
    else:
        print("Incorrect password")
else:
    print("Incorrect username ")

# Notes:
# The phrase below refere to equations
# Logical expresion e.g. (5+3/2)<5 and 9+2 == 12 both false
# or = If one is true then the whole equation is true.
# and = both need to be true for answer to equal true (usefull for usernames and passwords - have to get both correct to gain access.)
