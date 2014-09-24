# This is a python comment!
# The following is for python 2 and below. 
# In python 3 we would say: print ('our statement') 
# Other than that there isn't much to worry about btwn versions 2 & 3 for now!

# GETTNG STARTED WITH PYTHON

# The print method lets you print something in Python for others to see
# To do this simply type print followed by the string of characthers you
# want to print surrounded by quotes - YOU CAN USE DOULBE OR SINGLE QOUTES

# To combine multiple strings or variables, add a space and plus (+) sign. 

print 'Hello World!' + ' ' + 'There\'s a snake in my boot!'
# OUTPUT >>> Hello World! There's a snake in my boot!

# The word 'There's' is written with a \, like 'There\'s' - this tells
# the program to print the single quote instead of treating it as if the 
# string was ended - this is called 'escaping' a character. 

# A function is something that takes a value and uses that to return another 
# value. A method is a built in function, in some cases it can be built in by 
# the person who wrote the program. A function is written with an empty set
# of parenthesis, as in the type() function. These parenthesis are where you
# place the data that for method to use - that item or items are called 
# ARGUMENTS OR PARAMETERS. 

# The Type Function

# The type() method comes built in to the python language. It takes
# one argument and returns to us the type of data that the parameter is. 
# What's a data type?

# Remember the print method? When we used it we had to put 'hello world' 
# bewteen quotes - that's because we printed a 'string' of characters. 
# In programming, a string like 'donkey kong 64' is different than a number
# like 23, or, 64. 

# Let's use the type() method to demonstrate
print type('wazzzzup')
# >>> String

print type(64)
# >>> Number

print type('sixty four')
# >>> String

print type('64')
# >>> String


# SETTING VARIABLES

# A variable is an object you name that you can use to store data in. 
# You're probably used to them from algebra. You can use them to store
# just about anything in programming- from equations to functions to other
# variables and more.

# To set a variable just use a singe equals sign between the variable and what 
# you want to set it to. 

# Variables set the object on the left side of the equals sign to the oject on the 
# right side. 

dog = type(23)
print dog

