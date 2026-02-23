# In order to use this file, open a new terminal and type
# python day-01/main.py
# OR
# python3 day-01/main.py

# comment

# DOES A COMMENT DO ANYTHING???
# Not really... unless we want to write for ourselves and others

# VARIABLES

# store values

# declare a variable
my_variable = "Hello I am a variable"
# name      equal   value

# TERMINAL - COMMAND LINE

print( my_variable )

my_variable = "something else"

print( my_variable )

my_variable = "I have changed again"

print(my_variable)

# PYTHON IS LINEAR

my_second_var = "I am the second variable"
my_third_var = "I am the third variable"

print( my_second_var )

# DATA TYPES #

# STRING --> text

"I am a string"
'I am also a string'
"              " # <<< also a string
"123456789" # <<< also a string
"!@#$%^&*()" # <<< also a string

my_string = "Hello my name is \"Chett\""

# type will show you the data type
what_type = type( my_string )

print( what_type )

# concatenation a.k.a. adding strings together
brand_new_string = my_string + " and I like being a string"

# formatted string / f string
name = "Chett"
age = "21"
hobbies = "running around in the snow"

f"{ name } is {age} and likes {hobbies}"

# NUMBERS

# integer
type(21)
type(-21)
type(1000000000000000000000000)

# float
type( 2.1 )
type( 1.0 )

# math operations

1 + 1 # addition
2 - 1 # subtraction
3 * 3 # multiply
4 / 5 # divide
6 % 3 # modulo

# modulo lets you know what the remainder is of division between two numbers
15 % 3 # 0 remainder
16 % 3 # 1 remainder
7 % 3 # 1 remainder

# string-o-tizing data (stringify or string conversion)
str(15) # "15"

# BOOLEAN ###

True
False

# FUNCTION ##############

# D.R.Y. dont repeat yourself

result_1 = 12 % 3 == 0
print(result_1)
result_2 = 55 % 3 == 0
print(result_2)
result_3 = 5678 % 3 == 0
print(result_3)
result_4 = 92 % 3 == 0
print(result_4)
result_5 = 90 % 3 == 0
print(result_5)
result_6 = 9000 % 3 == 0
print(result_6)
result_7 = 13 % 3 == 0
print(result_7)

# defining a function
# `number` is a an argument / paremeter
def is_divisible_by_three(number):
    result = number % 3 == 0
    print(result)

# calling the function
is_divisible_by_three(12)
is_divisible_by_three(55)
is_divisible_by_three(5678)

# function without an argument
def say_hello():
    print("Hello world!")

# getting data from a function
def is_divisible_by_four(number):
    result = number % 4 == 0
    return result
# return gives data out of the function and completes the function

result = say_hello()
# result is nothing

result = is_divisible_by_four(4)
# result is True

def add(num1, num2):
    return num1 + num2

add(1,2) # return 3

def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

full_name("Bob", "Dylan") # "Bob Dylan"

# default argument
# "nothing" is the fallback value
def eat_breakfast( breakfast_item="nothing" ):
    breakfast_string = f"Yum yum eating {breakfast_item}. It's my favorite!"
    return breakfast_string

# return will give back data we use later somewhere else
result = eat_breakfast()

print(result)

def multiple_returns():
    return "thing 1"
    return "thing 2"
    return "thing 3"
    return "thing 4"
# only the first return triggers
# everything after a return is triggered in a function is DEAD CODE


# MINI EXERCISES -------------

# 1 - FULL_NAME #########

# Build a function `full_name()` which accepts two arguments, `first_name` and `last_name`.
# This function capitalizes the first letter of each and then formats them so they're together.
# The function returns the new string. Save the new string to a variable and `print` it to confirm it works.

# Examples:
# full_name("bob", "marley") --> "Bob Marley"
# full_name("elton", "john") --> "Elton John"

def full_name(first_name, last_name):
    return f"{ first_name.capitalize() } { last_name.capitalize() }"

# the .capitalize is a special function called a method

result = full_name("bob", "marley")
print(result)


# 2 - MAKE_SANDWICH ######

# Build a function `make_sandwich()` which accepts arguments for `protein`, `cheese`, `sauce`, and `other`.
# This function returns a string formatted like this: "I made a sandwich with {protein} with {cheese} cheese, {sauce}, and {other}".
# If no cheese is given, default to `american`.
# If no sauce is given default to `mayo`.
# If no `other` is given, default to `nothing else`.

# Examples:
# make_sandwich("ham", "swiss", "ketchup", "lettuce")
# --> "I made a sandwich with ham with swiss cheese, ketchup, and lettuce"
# make_sandwich("bacon")
# --> "I made a sandwich with ham with american cheese, mayo, and nothing else"

#                 protein is required
def make_sandwich(protein, cheese="american", sauce="mayo", other="nothing else"):
    return f"I made a sandwich with {protein} with {cheese} cheese, {sauce}, and {other}"

result = make_sandwich("turkey")

print( result )

# keyword arguments
# make_sandwich(cheese="swiss", protein="tofu", sauce="thousand island dressing", other="jalapenos")


def login(username, password):
#         condition           and means both must match!
    if (username == "chett" and password == "password123"):
        # block of code where stuff happens when the `if` is True
        return "user authenticated"
    else:
        # block of code where stuff happens when the `if` is False
        return "invalid username or password"
    
# if (True):
#     do stuff

# you don't need an else all the time

food = "hamburger"

# check the first thing
if (food == "vegetable"):
    print("what a healthy meal")
# if the first thing isn't true, check the second thing
elif (food == "candy"):
    print("yum it's candy")
# if the second thing isn't true, check the third thing
elif (food == "hamburger"):
    print("tasty hamburger")
# finally do the else if nothing else triggered
else:
    print("I don't want it")


# TRUTHINESS
# every value if it needs to be evaluated as "True" or "False" when it comes to an if statement has a "truthiness" to it

bool(1) # True
bool(0) # False
# 0 == 0% True, 1 == 100% True


# CONDITIONAL OPERATORS