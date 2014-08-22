# Methods are built-in functions that come with the language.
# Python has lots of them, like most languages

# The first method is the .upper() method
# We write it with empty parenthesis to let us know
# that it's a function. 

# .upper() will make a new string that is just like
# the old but with all the letters capitalized

my_friend = 'monkey'
new_word = my_friend.upper()
print new_word
# MONKEY


# .find()
# This method works just like our find method

find_k = my_friend.find('k')
print find_k
# 3

# We get the answer 3: which is the index in the
# string where .find() found 'k'. If it did not find
# any k's, the program would have returned false


# More find examples

find_key = my_friend.find('key')
print find_key
# 3 (the starting index where it found the string)


# .find() also takes a second argument of
# where in the string to start looking

find_e = my_friend.find('e', 3)
print find_e
#   4

# finally we can give it a 3rd agument of where
# to stop looking

find_n = my_friend.find('n', 1 ,5)
print find_n
#  2

