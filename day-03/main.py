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

# Build a class for `Car`. This class begins with attributes `make` & `model`. I would also like you to give your car an attribute `gallons_in_tank` which starts at 0.

# Car(make="Toyota", model="Corolla")

# Please build an `__init__` method for the car which accepts a `make` and `model`.

# Build a `__repr__` method which shows relevant details about the car.

# Build a `full_description` method which returns the `make` and `model` together like this:
# Example: "Toyota Corolla"

# Build a `fill_tank` method which sets the `gallons_in_tank` to 20.

# Build a `drive` method which reduces the `gallons_in_tank` by 10.
# BONUS: The `gallons_in_tank` shouldn't go below 0.

# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST
# RETURN AT 12:45 EST