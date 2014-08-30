# += Is something you will see commonly. It means that
# something equals itself plus whatever you add to it
# so x = x + 1   is the same as 
# x += 1
# and x = x + 12  is the same as
# x += 12

# Lets use it to add all the numbers in a list
def add_it_all(something):
	total = 0
	for x in something:
		total += x
		return total

# this is acutally such a commonly used loop that python 
# includes it in the sum() function

x = [2, 2, 4]
sum(x)
# >>> 8


######################################################

# Deleting an element from a list

# There's lots of ways to do this, the first is through
# the pop() method

# This will remove the element from the list at index 1
# and return the object it removed.

x.pop(1)


# If you wanted the element to delete the object but 
# didn't need the deleted object returned from the function,
# you can just use delete, like this:

x.delete[1]

# In you knew the object but not the index, you can
# remove that from the list by the remove function

x.remove('4')

# to remove more than one element you can use del() with
# a slice index like we used earlier

my_list = [1, 2, 3, 4, 5, 6, 7]

del my_list[2:5]

# >>> removes elemts with index 2, 3 and 4 but NOT 5!!!

############################################

# Lists vs Strings

# Strings are sequences of characters and lists are
# sequences of values - but a list of characters is not
# the same as a string!

# You can convert a string to a list of characters like this:


my_string = "dogs"
string_list = list(my_string)
print string_list
# >>>> ['d', 'o', 'g', 's']

##################################################

# Splitting Strings
# Use the split function to separate things split w/ a common characters

#Example

word = 'dog-dog-dog'
split_item = '-'
word.split(split_item)
