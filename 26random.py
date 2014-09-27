# A program is determinisitic if it is known what the outcome will
# be. It in indeterministic if you don't know what the result will be -
# this type is not so common, but is useful in games and other things. 

# In programming it is really hard to get true random, but
# there is a built in module that gives us something really really
# close to random, which is really good enough for nearly any 
# practical use.

# Example

# Use the random module
import random

for i in range(15)
	x = random.random() 
	print x


# Random Integer

# The function randint() takes two numbers and generates a random number
# between the two

random.randint(3, 17)

random.randint(6, 15)


# Random Choice

# random.choice() lets you select a random object out of a set

# Example

myList = [4, 5, 6]
random.choice(myList)
# >>> 6
random.choice(myList)
# >>> 5


# The random module also has functions to generate random values
# from continuous distributions, including Gaussian, expoenential,
# gamma and more





