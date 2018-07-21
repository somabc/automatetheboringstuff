Q1

Why are functions advantageous to have in your programs?
Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.

Q2 

When does the code in a function execute: when the function is defined or when the function is called?
The code in a function executes when the function is called, not when the function is defined.

Q3

What statement creates a function?
The def statement defines (that is, creates) a function.

Q4

What is the difference between a function and a function call?
A function consists of the def statement and the code in its def clause.
A function call is what moves the program execution into the function, and the function call evaluates to the function's return value.

Q5

How many global scopes are there in a Python program? How many local scopes?
There is one global scope, and a local scope is created whenever a function is called.

Q6

What happens to variables in a local scope when the function call returns?
When a function returns, the local scope is destroyed, and all the variables in it are forgotten.

Q7

What is a return value? Can a return value be part of an expression?
A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.

Q8

If a function does not have a return statement, what is the return value of a call to that function?
If there is no return statement for a function, its return value is None.

Q9

How can you force a variable in a function to refer to the global variable?
A global statement will force a variable in a function to refer to the global variable.

Q10

What is the data type of None?
The data type of None is NoneType.

Q11

What does the import areallyourpetsnamederic statement do?
That import statement imports a module named areallyourpetsnamederic. (This isn't a real Python module, by the way.)

Q12

If you had a function named bacon() in a module named spam, how would you call it after importing spam?
This function can be called with spam.bacon().

Q13

How can you prevent a program from crashing when it gets an error?
Place the line of code that might cause an error in a try clause.

Q14

What goes in the try clause? What goes in the except clause?
The code that could potentially cause an error goes in the try clause.

Q15

The code that executes if an error happens goes in the except clause.

