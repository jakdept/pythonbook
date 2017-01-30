>1. What is `[]`?

An empty list.

>2. How would you assign the value `'hello'` as the third value in a list stored in a variable named spam? (Assume spam contains `[2, 4, 6, 8, 10]`.)

`spam[2] = 'hello'`

>#### For the following three questions, let’s say spam contains the list `['a','b', 'c', 'd']`.
>3. What does `spam[int(int('3' * 2) / 11)]` evaluate to?

`spam[int(int('3' * 2) / 11)]` => `spam[int(int('33') / 11)]` =>

`spam[int(33 / 11)]` => `spam[int(3.0)]` => `spam[3]` => `'d'`

> 4. What does `spam[-1]` evaluate to?

`'d'`

> 5. What does `spam[:2]` evaluate to?

`['a','b']`

> #### For the following three questions, let’s say bacon contains the list `[3.14, 'cat', 11, 'cat', True]`.
> 6. What does `bacon.index('cat')` evaluate to?

`1`
> 7. What does `bacon.append(99)` make the list value in bacon look like?

`[3.14, 'cat', 11, 'cat', True, 99]`

> 8. What does `bacon.remove('cat')` make the list value in bacon look like?

`[3.14, 11, 'cat', True, 99]`

> 9. What are the operators for list concatenation and list replication?

Concatenation is `+`, Replication is `*`

> 10. What is the difference between the `append()` and `insert()` list methods?

`append()` adds to the end of the list
`insert()` adds to the specified position within the list (making the list longer)

> 11. What are two ways to remove values from a list?

`del list[5]`

`list.remove('item')`

> 12. Name a few ways that list values are similar to string values.

Lists can be indexed and sliced.

> 13. What is the difference between lists and tuples?

tuples are immutable, lists are mutable.

> 14. How do you type the tuple value that has just the integer value `42` in it?

A tuple is a tuple, no matter what is in it.

> 15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?

`tuple(list)`

`list(tuple)`

> 16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?

A reference to the list.

> 17. What is the difference between `copy.copy()` and `copy.deepcopy()`?

`copy.copy()` is a shallow copy, if it is called on a list it copies the contents of the list.
However, if the list contains another list, or another reference type, the reference is copied, not the underlying data.
As such, after a few layers, lists that have been copied are not independent - modifying one location modifies the other.

`copy.deepcopy()` recursively copies all data structures, allocating new data structures and putting the values in the new location.
A list that was deep copied is guarenteed independent of the original list.