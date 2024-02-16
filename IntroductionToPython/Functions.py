# Function is a reusable block of code defined using 'def' that performs
#   a specific tast by taking input, priccessing it and often returning a 
#   result.

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units():
    print(f"15 days are {15 * calculation_to_units} {name_of_unit}")

days_to_units()   

# Function with Parameters is a reusable block of code that accepts 
#   input values, known as parameters or arguments, when it's called. 
#   These parameters provide data for the function to work with, allowing 
#   it to perform tasks using the provided values.

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")

days_to_units(25) 
days_to_units(35) 

# Function - Two Parameters
calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(45, "Awesome!") 
days_to_units(55, "Looks good :)") 
