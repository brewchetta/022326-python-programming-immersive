# SCOPE

my_global_var = "I am a global variable"

def i_have_local_stuff():
    # START OF FUNCTION
    print(my_global_var)
    # the local variable is locked inside the function
    local_var = "I am local"
    print(local_var)
    # END OF FUNCTION

# this is fine though
print(my_global_var)

# this will error out because the local variable is not in scope
# print(local_var)


we_all_do_this = "breathe"

def france():
    # this doesnt overwrite the global it makes a LOCAL variable
    we_all_do_this = "oui oui baguette"
    print(we_all_do_this)

def france_two():
    # this WILL overwrite the global
    global we_all_do_this
    we_all_do_this = "oui oui baguette"
    print(we_all_do_this)    


# LISTS - (ARRAY)

# data structure - a data type that holds other data types


fruits_list = ["apple", "banana", "starfruit", "dragonfruit", "kiwi"]

# how to get the length of the list
len( fruits_list )

# USING INDEXES
fruits_list[0] # "apple"
fruits_list[2] # "starfruit"

# we can also count from the back
fruits_list[-1]

fruits_list.append("grape")
fruits_list.append("durian")

# remove the last item
fruits_list.pop()

# removing a specific item
fruits_list.remove("banana")

# two ways of removing based on an index
fruits_list.pop(1)
del fruits_list[1]

# changing data
fruits_list[0] = "banana"

# slicing data




# MINI EXERCISES

cheese_list = ["havarti", "swiss", "goat", "muenster"]

# 1. For the list, add "american" to the end of the list twice.

cheese_list.append("american")
cheese_list.append("american")

# 2. Change "goat" to "pepperjack". 

cheese_list[2] = "pepperjack"

# OR

# cheese_list.remove("goat")
# cheese_list.append("pepperjack")

# 3. Remove the extra "american" from the end of the list.

cheese_list.pop()
# OR
# cheese_list.remove("american")
# OR
# del cheese_list[5]

# 4. Remove "havarti".

cheese_list.remove("havarti")
# OR
# cheese_list.pop(0)

# 5. Print the first half of the list (and only the first half!)

cheese_list[0:2]

# extends will add a second array to the first
cheese_list.extend( ["cheddar", "halloumi", "havarti"] )

# ["Swiss"
# "Pepperjack"
# "Muenster"
# "American"
# "Cheddar"
# "Halloumi"
# "Havarti"]

# LOOPS

def print_capitalized_cheese():
    index = 0

    while index < len(cheese_list):
        cheese = cheese_list[index]
        print( cheese.capitalize() )
        index += 1

def print_out_cheese_we_like():
    for cheese in cheese_list:
        print(f"I like {cheese}")

# iterables


# TUPLES

# a tuple cannot be changed after it's made
cheese_tuple = ("cheddar", "swiss", "havarti")

# this won't work!
# cheese_tuple.append("halloumi")
# cheese_tuple.pop()
# cheese_tuple[0] = "muenster"


# SET

# a set does not allow duplicates! this can be really helpful for getting rid of duplicate data

cheese_list.append("cheddar")
cheese_list.append("cheddar")
cheese_list.append("cheddar")
cheese_list.append("cheddar")
cheese_list.append("cheddar")

unique_cheeses = set( cheese_list )
# {'halloumi', 'pepperjack', 'muenster', 'american', 'monster', 'havarti', 'cheddar', 'swiss'}


# RANGE

range(12, 20)
# numbers 12 through 19

range(12)
# numbers 0 through 11

def add_cheddar_to_list():
    cheese_list.append("cheddar")

for _ in range(10000):
    add_cheddar_to_list()

for _ in range(10000):
    cheese_list.pop()


# MINI EXERCISES

# Create a new list:

car_brands = ["toyota", "chevrolet", "ford", "ford", "ford", "mitsubishi", "honda", "BMW"]

# 1. Transform the list into a `set` so that it removes the duplicates and then transform the `set` back into a `list`. Check that the `list` has no duplicates.

car_brands_set = set( car_brands )
unique_car_brands = list( car_brands_set )

# 2. Create a function `print_brands()` which will loop through the list and print each brand.

def print_brands():
    for brand in car_brands:
        print(brand)

# 3. Create a function `add_brand_to_list_num_times()` which accepts two arguments, `brand` and `num`. This will add the brand to `car_brands` a number of times equal to `num`.


def add_brand_to_list_num_times(brand, num):
    for x in range(num):
        car_brands.append(brand)


# DICTIONARIES

# key / value pairs that determine certain attributes tied to that dictionary
person = {
    "name": "Chett",
    "age": 21,
    "hobbies": [ "thinking about python", "looking at python", "coding python", "drinking" ]
}

# name, age, hobbies would all be keys
# "Chett", 21, [list of hobbies...] would all be values

# accessing information
person["name"]

# accessing nested information
person["hobbies"][0]

# we can change attributes
person["age"] = 22

# add a new key/value pair
person["occupation"] = "python obsessed instructor"

# heavily nested dictionaries
world = {
    "people": {
        "chett":{
            "name": "Chett",
            "age": 21,
            "hobbies": [ "thinking about python", "looking at python", "coding python", "drinking" ]
        }
    }
}

# accessing deeply nested data
world["people"]["chett"]["age"]

# list of dictionaries
people_list = [
    { "name": "Chett", "age": 21 },
    { "name": "Steve", "age": 32 },
    { "name": "Steph", "age": 45 },
    { "name": "Joe", "age": 62 },
]