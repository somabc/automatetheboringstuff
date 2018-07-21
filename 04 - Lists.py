Q1
What is []?
The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.

Q2
How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
spam = hello[2]

For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].

Q3
What does spam[int(int('3' * 2) // 11)] evaluate to?
d because spam = [3]

Q4
What does spam[-1] evaluate to?
'd' (Negative indexes count from the end.)

Q5
What does spam[:2] evaluate to?
['a', 'b']


For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

Q6
What does bacon.index('cat') evaluate to?
1 (second item in list)

Q7
What does bacon.append(99) make the list value in bacon look like?
[3.14, 'cat', 11, 'cat', True, 99]

Q8
What does bacon.remove('cat') make the list value in bacon look like?
[3.14, 11, 'cat', True, 99]

Q9
What are the operators for list concatenation and list replication?
The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)


Q10
What is the difference between the append() and insert() list methods?
While append() will add values only to the end of a list, insert() can add them anywhere in the list.

Q11
What are two ways to remove values from a list?
The del statement and the remove() list method are two ways to remove values from a list.

Q12
Name a few ways that list values are similar to string values.
Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.

Q13
What is the difference between lists and tuples?
Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, ( and ), while lists use the square brackets, [ and ].

Q14
How do you type the tuple value that has just the integer value 42 in it?
(42,) (The trailing comma is mandatory.)

Q15
How can you get the tuple form of a list value? How can you get the list form of a tuple value?
The tuple() and list() functions, respectively

Q16
Variables that "contain" list values don't actually contain lists directly. What do they contain instead?
They contain references to list values.

Q17
What is the difference between copy.copy() and copy.deepcopy()?
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.