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

cheeses_list = ["havarti", "swiss", "goat", "muenster"]

# 1. For the list, add "american" to the end of the list twice.

cheeses_list.append("american")
cheeses_list.append("american")

# 2. Change "goat" to "pepperjack". 

cheeses_list[2] = "pepperjack"

# OR

# cheeses_list.remove("goat")
# cheeses_list.append("pepperjack")

# 3. Remove the extra "american" from the end of the list.

cheeses_list.pop()
# OR
# cheeses_list.remove("american")
# OR
# del cheeses_list[5]

# 4. Remove "havarti".

cheeses_list.remove("havarti")
# OR
# cheeses_list.pop(0)

# 5. Print the first half of the list (and only the first half!)

cheeses_list[0:2]


















# LOOPS



# DICTIONARIES


