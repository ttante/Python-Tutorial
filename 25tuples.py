# Tuples are essentially an array or list, 
# except they are IMMUTABLE! - and they are sets of 
# 2 things: keys and values
# They look like this {'a': 0, 'b': 1, 'c': 3}
# In this tuple the KEYS are letters and the VALUES are numbers

# You can create a tuple by making a string with a trailing comma 
# Example:

myTuple = 'dog',

# Another way is to use the tuple() constructor method
# Example
newTuple = tuple()

# Don't use tuple as a variable name, since it's a built in method

# Most of the list functions and operators work on Tuples
anotherTuple = ('a', 'b', 'c', 'd')
print anotherTuple[0]
# >>>>  'a'

#####################################################

# Sometimes you will want to swap the values of 2 variables, 
# as in make a equal to b and b equal to a

# The original way to do that would be

a = 1
b = 2
temporary = a
a = b
b = temp

# >>>> a = 2, b = 1

# THIS IS NOT THE BEST WAY TO DO THIS:
# Instead use tuple assignment, like THIS

a, b = b, a 

# This makes sets the first element on the left side of the 
# equals sign to the first element on the right, as well as the
# second, and so on if there were more. 

#########################################################

# Tuples can be returned from a function, just like strings, 
# this gives that function the capability of returning multiple 
# values 

# Example
# The divmod() method, short for division modulo, divides one number
# by another and then returns a tuple of the quotient and the remainder

divmodExample = divmod(10, 3)
print divmodExample

# >>> (3, 1)



#######################################################

# You can make a function take a tuple as an argument. 
# Some built in methods only take a certain number of argumernts, 
# but some, like max(), which finds the max value in any given
# set, can take any number of arguments. 

# Example
var myNewTuple = tuple(2, 3, 6, 3 ,2, 3, 6)
max(*myNewTuple)
# >>> 6

# THE MAGIC LIES IN THE * IN FRONT OF myNewTuple - this 
# tells the function it is going to get a tuple of an unknown
# length. 



########################################################

# The Zip method

# The zip() method takes two sets of characters, like a list and 
# a string, and returns a list of tuples, where each tuple
# has an element from each set of characters. 

# Example

myList = [1, 2, 3]
myString = 'abc'
myZipped = zip(myList, myString)
# >>>  [(1, 'a'), (2, 'b'), (3, 'c')]

# IF ONE OF THE CHACTER SETS IS SHORTER THAN THE OTHER, zip() 
# WILL STOP AFTER THE LAST ITEM IN THE SHORTER SET

# We can now do this
for number, letter in myZipped
	print number, letter


# >>>  1 a 
# >>>  2 b
# >>>  3 c


#########################################################


# To traverse a set of characters with their index, use the enumerate() method

# Example

for index, element in enumerate('dog')
	print index, element

# >>> 0 d
# >>> 1 o
# >>> 2 g


###########################################################

# You can use the items() method to list all the items in a set of 
# tuples or items, but THE ORDER OF THE ITEMS WILL NOT COME IN ORDER
# The items will show up in a random order - it's just the way it goes.

###########################################################


# You can use a list of tuples to construct a new dictionary

tupleList = [('d', 0), ('o', 1), ('g', 2)]
newDictionary = dict(tupleList)
print newDictionary

# >>> {'d': 0, 'o': 1, 'g': 2}


# Now we can traverse items in a dictionary like this: 

for key, value in newDictionary.items():
	pring value, key
# >>> 0 d
# >>> 1 o
# >>> 2 g


##################################################

# The relational operators, like <, >, <=, and >= work with tuples
# and other sequences. They start with the first character, and if the
# first 2 elements are equal, it moves to the next until it finds two
# that are different

# Example

xx = (1, 2, 3)
yy = (1, 1, 3)
xx > yy
# >>> True 


aa = (1, 2, 3)
bb = (1, 2, 4)
aa >= bb 
# >>> False

#####################################################
 
# DSU - for sorting
# There's a convention called DSU which stands for
# DECORATE - a sequence with a list of tuples
# SORT - the tuples list
# UNDECORATE - take the sorted elements out of the sequence

# Example
# Sort a list of words from longest to shortest

def length_sort(words):
	wordHolder = []
	for word in words:
		wordHolder.append((len(word), word))

	sortHolder.sort(reverse=True)

	sortedWords = []
	for length, word in wordHolder:
		sortedWords.append(word)
	return sortedWords


# First we declare wordHolder and then run through the list of words
# and append each word to the wordHolder.

# Then we take the wordHolder, which is now a list of words, and
# we sort each one. 
# Finally, we append each item in the sorted list into a new one.

