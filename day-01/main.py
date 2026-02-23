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
# everything after a return is triggered is DEAD CODE