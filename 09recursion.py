# recursion is tough! 
# recursion is when a function call itself
# it may take a while to set in! don't worry it will come

#let do factorial, which is a number multiplied by
#every other number is is higher than except 0

# its also written as ! , so !3 is the factorial of 3
# !3 = ( 3 * 2 * 1)  which equals 6. 
# !2 = 2 and !4 = 24

# In math we can write this equation as 
# n! = n(n-1)!  
# 0 has a special factorial, it equals 1


# lets code this!

def factorial(x):
	if n == 0:
		return 1
	else: 
		recurse_step = factorial(x-1)
		result = n * recurse_step
		return result