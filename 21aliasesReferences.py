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


# In this case a and b are equivalent, but not identical


###########################

# Aliasing
# take our previous example, and then do this

a = b
b is a
# >>>> True


# If this object is mutable (change-able), then you could
# do this

b[0] = 25
print a
# >>> [25, 2]

# While this can be useful, its a double edge sword that can lead to trouble

