# In python you can make parameters that come with default
# values: when you do this, the user can leave out that
# parameter and any other one with a default value and the
# function will still work.

# Example
a = 5
b = 10
def addC(x, y, c=15):
	ab = a + b
	return ab + c


# Now call the function
addC(a, b)
# >>> 30

# Notice we can leave out the variable c and it's not a problem
# because the program has a value for it. 

# If you did give a value for c, you overwrite the default value
# for it - this is how built in methods have default settings.

d = 0
addC(a, b, d)
# >>> 15

