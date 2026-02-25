"""###EXERCISE: Human Class

Create a new class `Human` which has required attributes `first_name:str`, `last_name:str`, `age:int`, `address:str`, and `is_hungry:bool`.

Human(first_name="Chett", last_name="Tiller", age=21, address="somewhere", is_hungry=True)

A `Human` instance has a `__repr__` that shows their attributes.

A `Human` instance has a `full_name()` method which returns their `first_name` and `last_name` in a single string, for example `"Bob Dylan"`.

A `Human` instance has an `order_drinks()` method which either returns `"Party time!"` if their age is 21 or older and returns `"Denied"` if their age is 20 or younger.

A `Human` instance has an `eat()` method which sets their attribute `is_hungry` equal to `False`.

A `Human` instance has a `win_lottery()` method which sets their attribute `address` equal to `"Disneyworld"`.

A `Human` instance has a `change_first_name()` method which creates an input with the prompt `"Change Name >>>"`. When a user completes the input the `first_name` attribute changes to their input.

"""

class Human:
	
	def __init__(self, first_name, last_name, age, address, is_hungry):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.address = address
		self.is_hungry = is_hungry

	def full_name(self):
		return f"{self.first_name} {self.last_name}"

	def __repr__(self):
		return f"Human(full_name={ self.full_name() }, age={self.age}, address={self.address}, is_hungry={self.is_hungry})"
	
	def order_drinks(self):
		if self.age >= 21:
			return "Party time!"
		else:
			return "Denied"
		
	def eat(self):
		self.is_hungry = False

	def workout(self):
		self.is_hungry = True

	def win_lottery(self):
		self.address = "Disneyworld"

	def change_first_name(self):
		self.first_name = input("Change Name >>> ")
		

# END OF THE CLASS DEFINITION #


human_1 = Human(first_name="Chett", last_name="Tiller", age=21, address="NYC", is_hungry=False)


# BONUS: BUILD THE LOTTO

from random import randint

list_of_numbers = [1,2,3,4,5]

# build a fn to input a list of numbers and check if they are winning lotto numbers
def check_lottery(list_of_numbers):
	# start with empty list
	winning_numbers = []
	# 5 times add a random number to winning_numbers
	for _ in range(5):
		random_number = randint(1, 70)
		winning_numbers.append(random_number)
	# if this is equal to the argument we win, otherwise we lose
	if list_of_numbers == winning_numbers:
		return "WINNER!!!"
	else:
		return f"try again next week... WINNING NUMBERS WERE: {winning_numbers}"