# Automate the Boring Stuff with Python
## Chapter 5 Questions

> 1. What does the code for an empty dictionary look like?

```
{}
emptyDictionary = {}
```

> 2. What does a dictionary value with a key `'foo'` and a value `42` look like?

```
{'foo':42}
emptyDictionary = {'foo':42}
```

> 3. What is the main difference between a dictionary and a list?

A dictionary is a key-value list - keys pointing to values. There is no order to the list.

> 4. What happens if you try to access `spam['foo']` if `spam` is `{'bar': 100}`?

You get a `KeyError`

> 5. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat'` in `spam` and `'cat'` in `spam.keys()`?

Nothing - the in statement compares against the keys.

> 6. If a dictionary is stored in `spam`, what is the difference between the expressions `'cat'` in `spam` and `'cat'` in `spam.values()`?

Everything - you cannot check for values with the in keyword.

> 7. What is a shortcut for the following code?
> 
> ```
> if 'color' not in spam:
>     spam['color'] = 'black'
> ```

```
spam.setdeefault('color', 'black')
```

> 8. What module and function can be used to "pretty print" dictionary values?

```
import pprint

pprint.pprint(dict)
```

