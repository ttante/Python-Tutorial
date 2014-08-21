# In programming there are arrays, which are ordered lists of things
# Arrays look like this ["5", "6", "7"]
# They can contain integers, strings, and even more arrays

# To create an array

my_array = ["6", "7", "boat"]

# to get "6", our first object

get_six = my_array[0]

# computers use 0 indexing... they start counting from 0
# so 0 is the first element in my_array which is "6"




# Strings like "dog" or "money" also can be maniuplated like arrays

bread = 'sourdough'
first_letter = bread[0]
second_letter = bread[1]

# len 
# len is a method, aka a built in function
# it gives you the length of a string 
print len(bread)

# Negative indexes!
# You can get the last letter in a string or array with -1
# Then the 2nd to last with -2, and so on

last_letter = bread[-1]
third_to_last_letter = bread[-3]