# import the math module
import math
def print_lyrics():
	print "got a wife and kids in baltimore jack"
	print "i went out for a ride and i never went back"
print_lyrics()

# call the function 'print lyrics as many times as you want!'
def repeat_lyrics():
	print_lyrics()
	print_lyrics()
repeat_lyrics()
line3 = 'Like a river that dont know where its flowing'

def print_twice(x):
	print(x)
	print(x)
print_twice(line3)

def finish_verse():
	print 'I took a wrong turn and I just kept going'

def verse1():
	print_lyrics()
	print(line3)
	finish_verse()

def blank_line():
	print ''

blank_line()
verse1()
blank_line()
print_twice("whats the time? d-d-diaper time! "*2)
print_twice(math.pi)
print_twice(math.sqrt(math.pi))

#import pi from math so you can just call pi
from math import pi
print pi

# import all from math so you can call it without
# calling the math module
from math import *
blank_line()
print 'cos * pi ='
print cos(pi)

def right_justify(x):
	print(' '*60 + x)
right_justify('doggy')

def do_twice(x):
	x()
	x()
def print_cat():
	print 'cat'
do_twice(print_cat)










