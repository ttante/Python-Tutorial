## a boolean function returns true or false
def is_divisible(x,y):
	if x % y == 0: 
		return True
	else:
		return False

print '15 and 5: '
print is_divisible(15, 5)

print '10 and 3: '
is_divisible(10, 3)