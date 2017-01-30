> 1. Which of the following are operators, and which are values?

> `*`

operator - binary operator

> `'hello'`

value - a string

> `-88.8`

value - a negative float

> `-`

operator - binary or unary depending on syntax

> `/`

operator - binary operator

> `+`

operator - binary or unary depending on syntax

> `5`

value - type int

> 2. Which of the following is a variable, and which is a string?

> `spam`

variable identifier

> `'spam'`

string

> 3. Name three data types.

* string
* int
* float
* decimal
* complex
* bool
* NoneType
* tuple
* list
* dict

> 4. What is an expression made up of? What do all expressions do?

Values and operators. Expressions are evaulated or reduced to one resulting value.

> 5. This chapter introduced assignment statements, like `spam = 10`. What is the difference between an expression and a statement?

An assignment statement does something with the resulting value - assigning it somewhere.

> 6. What does the variable bacon contain after the following code runs?
>```
>bacon = 20
>bacon + 1
>```

`20` - and the type is `int`

> 7. What should the following two expressions evaluate to?
>```
> `'spam' + 'spamspam'`
> `'spam' * 3`
>```

`'spamspamspam'`

> 8. Why is eggs a valid variable name while 100 is invalid?

The Python parser interperts 100 as an integer value, not a symbol name.

> 9. What three functions can be used to get the integer, foating-point number, or string version of a value?

`srt()`, `int()`, and `float()`

> 10. Why does this expression cause an error? How can you  x it?
>```
> 'I have eaten ' + 99 + ' burritos.'
>```

You cannot add an integer to strings. The following would work instead:

```
'I have eaten ' + str(99) + ' burritos.'
```

> Extra credit:
> Search online for the Python documentation for the len() function. It will be on a web page titled “Built-in Functions.” Skim the list of other functions Python has, look up what the round() function does, and experiment with it in the interactive shell.