# Lists can contain any type of data type, they can even 
# contain lists

# A list with no elemens is called an empty list,
# and you can create one like this
# my_list = []

sports = ['baseball', 'hockey', 'badminton']
numbers = [12, 80, 56]
print sports, numbers


# The most common way to traverse a list: for loop

for sport in sports:
	print "sport: ",
	print sport 


# Running a for loop on an empty array returns nothing

for x in []:
	print 'this will never be executed'

# Btw = a list counts as one element in a list,
# even thoug it may contain many items


#######################################################

# List operators

# The plus sign concatenates (combines)

list_a = [6, 3, 4]
list_b = [5, 7, 8, 9]

list_c = list_a + list_b
print list_c
# >>>  6345789

d = [1, 2, 3] * 3
print d
# >>> 123123123

# The slice operator works on lists

e = [4,5,6,7,8] 
print e[1:3]
# >>> ['5', '6']

print e[:3]
# >>> ['4', '5', '6']

# Since no number goes to it's respective end of the 
# array, no numbers on either side to both ends of
# the array: they return the whole array

print e[:]
# >>> [4,5,6,7,8]


##################################################

# List methods


# There are methods (built in functions) for lists

# Append
z = ['a', 'b', 'c']
z.append('d')
print z
# >>> ['a', 'b', 'c', 'd']


z2 = ['d', 'e', 'f']

z.extend(z2)
print z








