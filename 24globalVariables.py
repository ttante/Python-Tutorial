# A global vaiable is one that can be accessed from anywhere
# inside the program. 

# For example:

# If we create the variable 'myAge'
myAge = 26

# then we can make a function that accesses 'myAge'
# and modifies it. 

def myAgeNextYear(myAge):
	myAge == 27
	return myAge
# >>> 27

# BUT we can also change that value from a different function

def ageChange(myAge):
	myAge = myAge * 783434342
	return myAge
# >>> ?????

# The reason we can grab the myAge variable with any function
# is because it's located in the global scope. So how do
# you make something that's not in the global scope?


# The answer is to define things inside functions 

# Example 

def getMyAge():
	myNonGlobalAge = 26
	return myNonGlobalAge
# >>>> 26

# Here we declared my age INSIDE the function! So now if
# you tried this, WOULD NOT WORK!

# Example of what would NOT WORK!

def changeNonGlobalAge(myNonGlobalAge):
    myNonGlobalAge == 35

# >>>> WOULD NOT WORK!!!


# If you declare a global variable like this:
myGlobalVariable = 35

# You have to do this to use it in side another scope
def printGlobal():
	global myGlobalVariable
	print myGlobalVariable

# This happens with the statement 'global myGlobalVariable'

# Here;s an example of something that would not work

def addToGlobal():
	myGlobalVariable = myGlobalVariable + 1

# >>>>> WOULD NOT WORK!!!

# This does not work because the program thinks you
# are referring to a var that was created (defined) inside of 
# that function. 

