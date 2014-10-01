# TRANSIENT means a program has a short life span that just involves
# performing operations and ending after they return the results

# PERSISTENT programs run all the time or for a long time - basically
# every app these days is an example. 

# There are two ways store the data - there are two ways to 
# store data permanently for these types of programs - you
# can create actual text files or you can store things in a 
# database. 

# Recap: there are two types of persistent data, actual text files
# or data stored in databases.

# Let's get down with some text files.

# To write to a file, open it with mode 'w' as the 2nd paramater.
# If the file dosn't exist it creates a new one

# Example

fileOutput = open('output.txt', 'w')
print fileOutput
# >>> <open file 'output.txt', mode 'w' at RANDOMS_STRING>

# Use the write() method to insert data
newLine = 'Fish Sandwhich \n'
fileOutput.write(newLine)


# WHEN YOU ARE DONE YOU MUST CLOSE THE FILE!
# Use the close() method

fileOutput.close()


#####################################################

# The write() method only works with strings, so whatever
# data type you have must be converted to a string. 

# Example

myVar = 5
fileOutput.write(myVar)
# >>> ERROR

# This won't work because myVar is a number. 


# THE FORMAT OPERATOR  (%)

# Programming often uses something called the format operator, 
# this is something that comes from lots of other programming languages,
# perhaps most notable the C language.

# EXAMPLE

# The format operator lets us add numbers into strings

dalmations = 99
'number of dalmations: %d' % dalmations
# >>> 'number of dalmations: 99'

# What happeneded?
# Look at this line:
# 'number of dalmations: %d' % dalmations
# First we have the string, and then we have the format operator %
# followed by d.

# The 'd' stands for decimal - so this combination, %d, says 
# 'place an integer inside this string' - and then, after the 
# sring, we have '% dalmations' - that tells our string
# which variable that the interger is coming from.

# It's not my favorite programming convention, but you will
# see this done lots of times in programming. 


# Format Operator Types
# %d - Integer (stands for decimal)
# %s - String
# %g - Floating Point Int(Number with decimals, I don't
# know what the g stands for!)

###############################################################
# FILENAMES & PATHS

# Files come in directories, AKA folders. 
# CWD stands for current working directory

# The os module adds functions for the operating system you're using









