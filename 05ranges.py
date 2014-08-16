print 'i think im'
for i in range(7):
	print 'turning japanese i think im'
print 'i really think so'
five = 5
if five > 0:
	print 'five is greater than zero'

if five < 0:
	print 'nonsense happening now!'
elif five == 0:
	print 'other nonsense going down'
else:
	print 'five is def greater than zero',
	print 'and no shenanigans here'

print ' '
print 'the modulo operator is super useful'
print 'modulo 10 gives the right-most integer in a number'
print 'and modulo 100 gives the 2 right-most ints'

print ' '
print 'example % 10:',
print(575657 % 10)
print 'example % 100:',
print(747575757 % 100)

print 'some recursion fun!'

def recursive_countdown(x):
	if x <= 0:
		print 'blastoff!!!'
	else:
		print x
		recursive_countdown(x-1)

recursive_countdown(5)

def recursive_print(string, number):
	if number <= 0:
		return
	print string
	recursive_print(string, number-1)
recursive_print('turn down for what?', 4)

