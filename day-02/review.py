# Monday Review Practice #

# to run this in the terminal:

# python -i day-02/review.py

# the -i means it will run / load the file but also open a REPL at the end so we can continue interacting with variables and functions

# Define a new function create_full_name() which takes in two arguments: first_name and last_name as strings
# 	the function returns the first_name and last_name as a single string
# 	Example:	create_full_name("Bob", "Marley") >>> "Bob Marley"


def create_full_name(first_name, last_name):
    return f"{first_name} {last_name}"


# with inputs
# def create_full_name():
#     first_name = input("Enter first name: ")
#     last_name = input("Enter last name: ")

#     return f"{first_name} {last_name}"
#     # return first_name + " " + last_name


# Define a new function c_to_f() which takes in one argument: temp_celsius as a number
# 	the function returns the temperature as farenheit, you may return either an int or a float
# 	the formula for conversion is F = (C * 9/5) + 32
# 	Example:	c_to_f(30) >>> 86.0

def c_to_f(temp_celsius):
    return (temp_celsius * 9/5) + 32