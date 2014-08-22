# Lets take a quick look at looping to find something 
# again. 

letter = 'a'
word = 'boat'

def find(word, letter):
	index = 0
	while index < len(word):
		if word[index] == letter: 
			print 'letter found!'
			return
		index = index + 1
	return 'letter not found!'