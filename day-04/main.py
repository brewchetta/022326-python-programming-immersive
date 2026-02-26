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

import requests

def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json" }

    # try to do this
    try:
        response = requests.get(url, headers=headers)
        return response.json()
    except:
        return { "error": "Couldn't get a dad joke" }


# CRUD
# create    read    update        delete 
# POST      GET     PATCH/PUT     DELETE


# EXAMPLE COMMAND LINE INTERFACE APP

# retailer API
# API keys - special key / passcode to use an API

base_url = "https://www.fruityvice.com/api/fruit/"


# heredoc
"""
# Produce Pantry #

## USER STORIES ##
- user will be able to create a pantry of their own fruit
- user will be able to add fruit to the pantry
- user will be able to remove fruit from the pantry
- quick nutritional facts about a piece of fruit
-user will be able to view the type of fruit in the pantry

## API ##
https://www.fruityvice.com/api/fruit/

"""

# find the apple.py apple and take the apple_art from there
from apple import apple_art

# this is the program itself
class Application:

    # CLASS VARIABLES #
    base_url = "https://www.fruityvice.com/api/fruit/"
    running = True
    user_name = "anonymous"


    # RUN LOOP #
    # each method will be a specific functionality within the app
    def run(self):
        # first show the intro screen
        self.intro_screen()
        # then enter loop for running the app
        while self.running:
            self.main_menu()
        

    # INTRO SCREEN #
    def intro_screen(self):
        for line in apple_art:
            print(line)
        self.get_name()
        print(f"Welcome {self.user_name}!")
    
    def get_name(self):
        self.user_name = input("What is your name >>> ")


    # MAIN MENU #
    def main_menu(self):
        print("Make a choice:")
        print("1. Lookup a fruit")
        print("5. Exit")
        choice = input(">>> ")
        if choice == "1":
            self.fruit_lookup()
        elif choice == "5":
            self.running = False

    
    # LOOKUP #
    def fruit_lookup(self):
        print("What fruit would you like to lookup?")
        fruit = input(">>> ")
        # go request the fruit from the API
        self.get_fruit(fruit)

    def get_fruit(self, fruit):
        response = requests.get(self.base_url + fruit)
        fruit_data = response.json()
        self.pretty_print_fruit(fruit_data)
    
    def pretty_print_fruit(self, fruit_data):
        print(fruit_data["name"])
        print(fruit_data["family"])
        print(fruit_data["order"])
        print(fruit_data["genus"])





# start running the application instance!
app = Application() # we make a new instance of the app
app.run()