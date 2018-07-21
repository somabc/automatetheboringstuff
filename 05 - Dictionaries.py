Q:

1. What does the code for an empty dictionary look like?

dictionary = {}

Q:

2. What does a dictionary value with a key 'foo' and a value 42 look like?

dictionary = {'foo': 42}

Q:

3. What is the main difference between a dictionary and a list?
lists are an array of values and can be ordered and accessed. dictionaries are a key value store. Accessing a list is fast.
Q:

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
Error

Q:

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
No difference.

Q:

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.

Q:

7. What is a shortcut for the following code?


if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('color', 'black')

Q:

8. What module and function can be used to “pretty print” dictionary values?

pprint.pprint()