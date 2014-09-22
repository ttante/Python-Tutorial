# Chapter 11 - Page 121

# Dictionaries are like lists, but they're not numbered. 
# Instead they *contain a key and value, both created by 
# you: this is a key/value pair paradigm, its pretty common

# Crete A dictionary with no items

var myDict = dict()
print myDict
# >>> {}


# The curly braces {} represent a dictionary

myDict['dog'] = 'bark'
print myDict[]
# >>>> {'dog': 'bark'}

# You can access the key via the value or the value 
# via the key, like this

print myDict['dog']
# >>> 'bark'

# and

print myDict['bark']
# >>> 'dog'


# Since dictionaries aren't formally numbered, you can't
# even count on them to be in any certain order

# Example:
# Another way to make a dictionary
 
myDict2 = {'dog': 'bark', 'cat': 'meow', 'bird': 'chirp'}


# But if you print them, you might get

print myDict2
# >>>  { 'bird': 'chirp', 'dog': 'bark', 'cat': 'meow'}

# So don't depend on the order, you will get different 
# orders from different computers. But don't worry, 
# we don't need the order when dealing with dictionaries

# The len operator works on dictionaries, it gives you
# the number of key-value pairs in the dict, like this

len(myDict2)
# >>> 3


# The in operator works to find keys, it returns true
# if the phrase exists as a key, however it 
# WILL NOT return values. 

# Example

'dog' in myDict2
# >>> True

'bark' in myDict2
# >>> False


# To see if a value exists in a dictionary, call the 
# method values() on the dictionary: values() will 
# return all the values as a list, and you can search 
# that list with the 'in' operator

# Example

getValues = myDict2.values()
'bark' in getValues
# >>> True


##########################################################

# You can use a for statement to loop through the keys
# of a dictionary


myDict3 = {'dog': 'bark', 'cat': 'meow', 'bird': 'chirp'}

def print_hist(myDict3)
	for key in myDict3:
		print key, myDict3[key]


# Once again we can use for statements to loop through keys,
# but this does not work with values: to do that you have
# to do a reverse lookup

# Example
def reverse_lookup(myDict3, value):
	for key in myDict3:
		if myDict3[value] == key:
			return key;
	raise ValueError



