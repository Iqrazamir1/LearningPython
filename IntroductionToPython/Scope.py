# Global Scope is variables available from within any scope but
#  local variables are created inside functions. Example below. 

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

def scope_check ():
    print(name_of_unit)

days_to_units(45, "Awesome!") 
days_to_units(55, "Looks good :)") 
scope_check()
