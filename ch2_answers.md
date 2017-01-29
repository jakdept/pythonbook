> 1. What are the two values of the Boolean data type? How do you write them?

`True` and `False`

> 2. What are the three Boolean operators?

`not`, `and`, and `or`

> 3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).

| a     | b     | not a | a and b | a or b |
|-------|-------|-------|---------|--------|
| True  | True  | False | True    | True   |
| True  | False | False | True    | True   |
| False | True  | True  | False   | True   |
| False | False | True  | False   | False  |

> 4. What do the following expressions evaluate to?
> ```
> (5 > 4) and (3 == 5)
>```
`True and False` => `False`
>```
> not (5 > 4)
>```
`not True` => `False`
>```
> (5 > 4) or (3 == 5)
>```
`True or False` => `True`
>```
> not ((5 > 4) or (3 == 5))
>```
`not (True or False)` => `not True` => `False`
>```
> (True and True) and (True == False)
>```
`True and False` => `False`
>```
> (not False) or (not True)
> ```
`True or False` => `True`

> 5. What are the six comparison operators?

`==`, `!=`, `<`, `>`, `<=`, `>=`

> 6. What is the difference between the equal to operator and the assignment operator?

`==` (equality) returns `True` or `False` based on the conditions, `=` (assignment) assigns the value on the right to the value on the left.

> 7. Explain what a condition is and where you would use one.

A condition is something that evaulates to either true or false, and you often use them in `if` statements and `while` loops.

> 8. Identify the three blocks in this code:
> ```
> spam = 0
> if spam == 10:
>     print('eggs')
>     if spam > 5:
>         print('bacon')
>     else:
>         print('ham')
>     print('spam')
> print('spam')
> ```

```
     print('eggs')
     if spam > 5:
         print('bacon')
     else:
         print('ham')
     print('spam')
```

```
         print('bacon')
```

```
         print('ham')
```

> 9. Write code that prints `Hello` if `1` is stored in `spam`, prints `Howdy` if `2` is stored in `spam`, and prints `Greetings!` if anything else is stored in `spam`.

```
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
```

> 10. What can you press if your program is stuck in an infinite loop?

`ctrl+c`

> 11. What is the difference between break and continue?

`continue` jumps to the next execution of the current block, skipping the rest of the block.
`break` jumps past the end of the block, skipping the rest of the block.

> 12. What is the difference between `range(10)`, `range(0, 10)`, and `range(0, 10, 1)` in a for loop?

Nothing.
The one parameter format assumes a starting index of `0`.
The one and two parameter format assumes a incremental value of `+1`.

> 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

```
for number in range(1, 10):
    print(number)
```

```
number = 1
while number <= 10:
    print(number)
    number += 1
```

> 14. If you had a function named `bacon()` inside a module named `spam`, how would you call it after importing `spam`?

`spam.bacon()`

> Extra credit: Look up the `round()` and `abs()` functions on the Internet, and find out what they do. Experiment with them in the interactive shell.

`round()` rounds a `float` to the nearest `int`.
`abs()` takes a `float` or `int` and returns the absolute value.
