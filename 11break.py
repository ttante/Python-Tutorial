# break will jump you out of a loop

num = 2
huge_num = 10000
while num > huge_num:
	print num
	if huge_num % num == 0:
		break
	num = num + 1
	print 'this round: ',
	print num



# if type(userInput) == str:

