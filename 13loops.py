# For and while loops are used all the time in code
# They're often used for the traversal of a string -
# For instance if you want your program to traverse
# every character in a string to see if it is an illegal one.

# Here's how we do it:
# First we set our word equal to bread.
# Then we create an index to use to traverse
# through the string, and we will count all the
# time's the character 'u' appears in 'sourdough'
# by adding to it every time we find one. 
bread = 'sourdough'
index = 0
u_count = 0

while index < len(bread):
	x = bread[index]
	if x == "u":
		u_count = u_count + 1
	index = index + 1
print "Number of U's: ",
print u_count

# Another and often more convenient way is to 
# use a 'for' loop instead of a whie. The doifference
# is that a for loop is just a shorter and less detailed
# way of doing things, you can almost always use the other
# to accomplish a problem that one can do

# Here we will do the same thing as up above
index2 = 0
u_count2 = 0

for char in bread:
	if char == "u":
		u_count2 = u_count2 + 1
print "number of U's from the for loop: ",		
print u_count2		

# first things first, the variable char can be
# named whatever you want. So a for loop reads like
# for (whatever you want to call each char) in (variable we're traversing)
# You could really call it widnmills or mc_hammers 
#


# Here's a fun way to use concatenation (adding strings together)
# to finish names

prefixes = 'BCHMPRS'
suffix = 'at'


for letter in prefixes:
	print letter + suffix
