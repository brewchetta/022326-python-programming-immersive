# automated test - run script - test that your code works
# TDD - test driven development --> build your tests first to show how a product should work
# mvp - minimum viable product


# OBJECT ORIENTED PROGRAMMING VS FUNCTIONAL PROGRAMMING


# LIST COMPREHENSIONS

numbers_list = [1,2,3,4,5,6,7,8,9,10,11]
numbers_squared = [ each_number ** 3 for each_number in numbers_list ]
# numbers_squared = [1,4,9,16,25,36,49,64,81,100,121]

names_list = ["bob", "jim", "steve"]
capitalized_names = [ name.capitalize() for name in names_list ]

pizzas_list = [
    { "name": "Hawaiian", "price": 20.995 },
    { "name": "Deep Dish", "price": 50.99 },
    { "name": "Ol' Fashioned Cheese Pizza", "price": 15.99 }
]

# def format_pizza(pizza_dict):
#     do all the work to format the pizza
#     return the result

# formatted_pizzas = [ format_pizza(pizza) for pizza in pizzas_list ]


# LAMBDA FUNCTIONS

    # name             parameters
def normal_function(something):
    # body / instructions
    print(something)

# name.              paramaters  body/instructions
my_lamba_fn = lambda something: print(something)

# a normal function needs the return keyword to get data back
def square_number(x):
    return x ** 2

# a lambda automatically return its result right away
square_number = lambda x: x ** 2


















# PIP & REQUESTS









# EXAMPLE COMMAND LINE INTERFACE APP