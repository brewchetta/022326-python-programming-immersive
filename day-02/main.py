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

























# LISTS



# LOOPS



# DICTIONARIES


