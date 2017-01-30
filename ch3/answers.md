> 1. Why are functions advantageous to have in your programs?

Functions allow you to avoid duplicating code. Avoiding that makes writing the code easier, debugging the code easier, and updating the code easier.

> 2. When does the code in a function execute: when the function is defined or when the function is called?

When the function is called.

> 3. What statement creates a function?

`def`

> 4. What is the difference between a function and a function call?

A function is the definition of the function, it creates a set of instructions in memory.
A function call, or call to that function, actually executes those instructions.

> 5. How many global scopes are there in a Python program? How many local scopes?

There is one global scope, shared across the entire runtime.
There is a local scope local to every single line.

> 6. What happens to variables in a local scope when the function call returns?

The variable is destroyed - the memory allocations are released.

> 7. What is a return value? Can a return value be part of an expression?

A return value is the value returned from a function. It can be used in an expression.

> 8. If a function does not have a return statement, what is the return value of a call to that function?

`None` of type `NoneType`.

> 9. How can you force a variable in a function to refer to the global variable?

By adding the `global` keyboard before the variable name.

> 10. What is the data type of `None`?

`NoneType`

> 11. What does the import `areallyourpetsnamederic` statement do?

Parses the file named `areallyourpetsnamederic.py`.

> 12. If you had a function named `bacon()` in a module named spam, how would you call it after importing spam?

`spam.bacon()`

> 13. How can you prevent a program from crashing when it gets an error?

By using a `try` `catch` block.

> 14. What goes in the `try` clause? What goes in the `except` clause?

The `try` block contains the code that may fail.
The `catch` block contains the code to run when an error is encountered.
