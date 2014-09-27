# Let's make a program taht reads file and make a 
# histogram (occurrence counter) of each word in the
# file

# Add string methods
import string

def read_file(filename):
	hist = dict()
	myFile = open(filename)
	for line in myFile:
		read_line(line, hist)
	return hist

def read_line(line, hist):
	line = line.replace('-', ' ')

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace) 
		word = word.lower()

		hist[word] = hist.get(word, 0) + 1
myHistogram = read_file('filename.extension')


# Get the total number of words
def total_words(myHistogram):
	return sum(myHistogram.values())

# Get the number of different words
def different_words(myHistogram):
	return len(myHistogram)


# Get the most common words
def most_common(myHistogram):
	words = []
	for key, value in myHistogram.items():
		words.append((value, key))

	words.sort(reverse=True)
	return words

# Print 15 most common words
words = most_common(myHistogram)
print 'Most common words:'
for freq, word in words[0:15]:
	print word, '\t', freq





