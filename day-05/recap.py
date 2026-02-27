# RECAP #

# TOPICS TO RECAP #

# variables
    # strings
    # numbers
    # booleans
# functions
    # nested function calls *
# conditionals
# lists *
    # list methods
    # list comprehension
    # nested lists *
# dictionaries
    # nested dictionaries *
# tuples / sets
# classes
    # OOP
    # instance methods
    # class methods
# modules & libraries
# requests
    # using APIs *
# code readability *
# debugging *


# venv
# command line fluency

# LISTS #

                # 0           1       2               3         4
sandwich_sides = ["fries", "chips", "pickle spears", "soup", "salad"]
# ordered & zero indexed


# LIST METHODS #

# CRYPTO LIST
# name:str
# buying_price: float
# location: str - site crypto can be bought
# three_month_history:list - updated at the first of each month
crypto_list = [
    {
        "name": "Bitcoin",
        "buying_price": 68000,
        "location": "trading view",
        "three_month_history": [900000, 100000, 120000]
    },
    {
        "name": "XLM",
        "buying_price": 0.15,
        "location": "trading view",
        "three_month_history": [0.16, 0.14, 0.15]
    },
    {
        "name": "XRP",
        "buying_price": 10,
        "location": "trading view",
        "three_month_history": [9, 8, 7]
    }
]

import ipdb


def search_crypto_by_price(min=0, max=float('inf')):

    # what values / inputs do I need in order to do this
        # list, min value, max value
    # OUTPUT: filtered list between the minimum and maximum
    # look through the list
    #     for each item look at buying_price
    #     for each price see if it's between min and max
    #     if it is, gets added to a new list

    is_price_acceptable = lambda crypto_dict: min < crypto_dict["buying_price"] < max
    ipdb.set_trace()
    return list( filter( is_price_acceptable, crypto_list ) )


# TECH DEBT
# good practices, refactors, documentation
# VS
# the fast paced demands of the work