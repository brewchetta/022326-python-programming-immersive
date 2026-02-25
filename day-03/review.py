# Tuesday Review #

# Define a new function open_thieves_cave() which takes in one argument: passphrase as a string
# 	the function returns True if the passphrase is "open sesame" and False if the passphrase is anything else
# 	Example:	open_thieves_cave("open sesame") >>> True
# 	Example:	open_thieves_cave("speak friend and enter") >>> False

def open_thieves_cave(passphrase):
      return passphrase == "open sesame"

# Define a new function fungus_among_us() which accepts a list `plants` as an argument
#   return True if the function contains the string "fungus" and False if not
# 	don't overthink this one, there's a very simple method to doing it...
#   Example: fungus_among_us( ["tree", "flower", "fungus", "moss"] ) >>> True

example_plants_list = ["tree", "flower", "fungus", "moss"]

def fungus_amongus(plants):
    return "fungus" in plants

# Define a new function total_bill() which accepts a list of numbers `item_costs`
#   return the sum total of all items in the list
#   Example: total_bill( [6, 9.99, 20] ) >>> 35.99

def total_bill(item_costs):
	return sum(item_costs)

# Define a new function halfway_there() which accepts a list of arbitrary data `items` longer than 1 item
#   insert the string "HALFWAY" at the middle of the list and return the altered list
# 	when inserting, you will need to make sure your index is an integer...
#   Example: halfway_there( [1,2,3,4,5,6] ) >>> [1,2,3,"HALFWAY",4,5,6]

def halfway_there(list_items):
    length = len( list_items )
    halfway_index = int( length / 2 )
    print(halfway_index)
    list_items.insert(halfway_index, "HALFWAY")
    return list_items