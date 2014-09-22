# There are many operators for lists, and it is 
# important to know which ones modify the original 
# list and which ones don't

# Example
# The append() method modifies, the + operator makes a new list

list1 = [1, 2, 3, 4]
list2 = list1.append(5)
print list1
# >>> [1, 2, 3, 4, 5]
print list2

