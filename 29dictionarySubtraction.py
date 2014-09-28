# Lets make a function that takes two dictionaries of words and finds out 
# which words in one dictionary will not be in the other

# This is also known as list subtraction

# Lets take 2 dicts, d1 and d2, and return a new 
# dictionary of all the keys from d1 that are not in d2

# We only need keys here, not the values, so we set all
# values to None

def dictSubtract(d1, d1):
	container = dict()
	for key in d1: 
		if key not in d2:
			container[key] = None
	return res


# To words that are not in a given text file, let's call our 29textFile.text,
# we build a historgram for textFile.txt, then subtract

# Example
myTextFile = process_file('words.txt')
diff = subtract(hist, myTextFile)

print "Words"
for word in myTextFile.keys():
	print word,

