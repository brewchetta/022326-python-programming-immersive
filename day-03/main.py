# CLASSES

# a representation of a real world thing
robot = {
    "name": "WALL-E",
    "main_objective": "collect trash, make cubes",
    "description": "very square lookin"
}

# class --> factory for creating data objects which have certain attributes AND behaviors


# lower_snake_case ---> my_variable_name

# classes use UpperCamelCase ---> MyVariableName

# this is technically a Robot factory / blueprint
# it allows us to create instances of Robots
class Robot:

    # init stands for initialize
    # this is a special method that gets called when we build a robot
    # dunder methods --> double under (score) --> special methods
    # this method triggers whenever we make a new robot
    def __init__(self, name, description):
        self.name = name
        self.description = description

    # representation method
    def __repr__(self):
        return f"Robot(name={self.name}, description={self.description})"
    
    # self is the robot itself
    def compute(self):
        return "...COMPUTING..."
    
    def walk(self):
        return "...BEEP BOOP WALKING..."

    # def buy_bitcoin(amount):
        # all the steps to buy that much bitcoin and add it to the wallet

    def who_am_i(self):
        return f"I AM {self}"
    
    def give_name(self, given_name):
        self.name = given_name

    def give_description(self, given_description):
        self.description = given_description


# this builds a new robot instance
wall_e = Robot(name="WALL-E", description="kinda square")
t_1000 = Robot(name="T-1000", description="Arnold Schwarzeneger")


# MINI-EXERCISE

# Build a class for `Car`. This class begins with attributes `make` & `model`. Also give your car an attribute `gallons_in_tank` which starts at 0 when the car is initialized.


# Please build an `__init__` method for the car which accepts a `make` and `model`.

# Build a `__repr__` method which shows relevant details about the car.

# Build a `full_description` method which returns the `make` and `model` together like this:
# Example: "Toyota Corolla"

# Build a `fill_tank` method which sets the `gallons_in_tank` to 20.

# Build a `drive` method which reduces the `gallons_in_tank` by 10.
# BONUS: The `gallons_in_tank` shouldn't go below 0.

class Car:

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.gallons_in_tank = 0

    def __repr__(self):
        return f"Car(make={self.make}, model={self.model}, gallons_in_tank={self.gallons_in_tank})"
    
    def full_description(self):
        return f"{self.make} {self.model} with {self.gallons_in_tank} in the tank"
    
    def fill_tank(self):
        self.gallons_in_tank = 20

    # def drive(self):
    #     while self.gallons_in_tank != 0:
    #         self.gallons_in_tank -= 10

    # def drive(self):
    #     self.gallons_in_tank -= 10
    #     if self.gallons_in_tank < 0:
    #         self.gallons_in_tank = 0

    def drive(self):
        gas_calculation = self.gallons_in_tank - 10
        self.gallons_in_tank = max(0, gas_calculation)

corolla = Car(make="Toyota", model="Corolla")




# CLASS METHODS AND CLASS ATTRIBUTES

class House:

    # class attribute
    structure_type = "Residential"
    
    # this will eventually be a list of every house we've initialized with __init__
    all_houses = [] # House.all_houses

    current_id = 1

    def __init__(self, square_footage, num_bedrooms, num_baths):
        # each house gets a unique id
        self.id = House.current_id
        House.current_id += 1
        # other attributes
        self.square_footage = square_footage
        self.num_bedrooms = num_bedrooms
        self.num_baths = num_baths
        # the new house gets added to House.all_houses
        House.all_houses.append(self)

    def __repr__(self):
        return f"House(square_footage={self.square_footage}, num_bedrooms={self.num_bedrooms}, num_baths={self.num_baths})"
    
    # decorator... it alters / changes how the function coming after it works
    # the @classmethod means it's callable by House and not an individual like house_1
    @classmethod
    def demolish_all_houses(cls):
        # cls is House
        cls.all_houses = []


house_1 = House(40000, 6, 1)
house_2 = House(100, 0, 1)


# RANDOM & MODULES

# get extra code from a MODULE
import random

# run this loop 10 times
for _ in range(10):
    # get random values --> randint stands for random integer
    # randint gets a number between the first and second number
    square_footage = random.randint(1000, 20000)
    num_bedrooms = random.randint(1, 6)
    num_bathrooms = random.randint(1, 12)
    # build a house
    House(square_footage, num_bedrooms, num_bathrooms)

# using random.choice to get a random pizza topping
pizza_toppings = ["cheese", "pepperoni", "pineapple", "mushroom", "ham"]
choice_1 = random.choice( pizza_toppings )
choice_2 = random.choice( pizza_toppings )
