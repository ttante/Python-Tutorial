# If we do this

a = "dog"
b = "dog"

# We know they both refer to a sting of "dog", we don't 
# know if they refer to the exact same string

# To see if two variables reference the same object,
# we can do this: 

a is b
# >>> True

# In this example, python created just one string object
# and let two variables refer to it. 

# This can be avoided by creating lists, which always returns
# a new object. 

a = [1, 2]
b = [1, 2]
a is b
# >>>> False

