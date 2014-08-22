# In python, strings are immutable! This means they cannot
# be changed or altered once they have been created.

# In other programming languages, you can do have a 
# word, for example word = "dog" and you can changed
# a letter in the word through the index retrieval
# we just learned, so you could do 
# word[0] = "b"  and change "dog" to "bog"
# BUT NOT IN PYTHON!!

# In python the best we can do is make a new string
# For example 

word = "dog"
new_word = "b" + word[1:]
print new_word
# "bog"



