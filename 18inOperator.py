# The in operator takes 2 stings and returns true if 
# the first string appears in the second
letter_a = "a"
letter_b = "b"

taco = 'taco'
bell = 'bell'

a_in_taco = letter_a in taco
print a_in_taco
# true
b_in_taco = letter_b in taco 
print b_in_taco
# false



# Here's a program that uses an 'if' statement to 
# see if a character is in both words

burrito = 'burrito'
def in_both (bell, burrito):
	for letter in bell:
		if letter in burrito:
			print letter_b
# >>> b




# String operators
# You can use greater than > and less than < op erators to compare
# strings as well! Capital letters come first, then alphabetical order


if bell > taco:
	print "true"
# >>> true

