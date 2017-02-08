> 1. What is the function that creates Regex objects?

`re.compile()`

> 2. Why are raw strings often used when creating Regex objects?

Raw strings can be abstraced away as a constant in the code.

> 3. What does the `search()` method return?

A `re.match` object

> 4. How do you get the actual strings that match the pattern from a Match object?

`match.groups()`

> 5. In the regex created from `r'(\d\d\d)-(\d\d\d-\d\d\d\d)'`, what does group 0 cover? Group 1? Group 2?

* Group 0 returns the entire match
* Group 1 returns the area code - the 3 digit prefix
* Group 2 returns the local phone number - the next 7 digits

> 6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?

* `.` represents any character except a whitespace.
* `\.` represents an actual period character.
* `()` is used to group portions of regex.
* `\(` and `\)` represents the paranthenses characters.

> 7. The `findall()` method returns a list of strings or a list of tuples of strings. What makes it return one or the other?

If there are no groups in the regex, all matches for the regex are returned as a list of strings.
If there are groups within the regex pattern, each tuple contains the entire match then all groups.

> 8. What does the `|` character signify in regular expressions?

An `or` condition.

> 9. What two things does the `?` character signify in regular expressions?

* The previous itme could have been there or not been there, but not repeated.
* Marking a match as non-greedy (greedy is default).

> 10. What is the difference between the `+` and `*` characters in regular expressions?

* `*` can match 0 or 1 or many.
* `+` can match 1 or many.

> 11. What is the difference between `{3}` and `{3,5}` in regular expressions?

* `{3}` matches exactly 3 occurances of the previous item.
* `{3,5}` matches 3, 4, or 5 occurances of the previous item.

> 12. What do the `\d`, `\w`, and `\s` shorthand character classes signify in regular expressions?

* `\d` is a stand in for any single digit.
* `\w` is a stand in for any single alpha-num.
* `\s` is a standin for any single whitespace.

> 13. What do the `\D`, `\W`, and `\S` shorthand character classes signify in regular expressions?

* `\D` is a standing for anything other than a numberical digit.
* `\W` matches anything that is not an alpha-num.
* `\S` matches any non-whitespace.

> 14. How do you make a regular expression case-insensitive?

Pass the flag `re.I` to `re.compile()`.

> 15. What does the `.` character normally match? What does it match if `re.DOTALL` is passed as the second argument to `re.compile()`?

Everything except a newline will match a `.`, unless `re.DOTALL` is passed in which case it matches anything.

> 16. What is the difference between `.*` and `.*?`?

Nothing. `.*?` is a creative way of saying it though. For that matter, `.+?` is the same.

> 17. What is the character class syntax to match all numbers and lowercase letters?

`[a-z0-9]`

> 18. If `numRegex = re.compile(r'\d+')`, what will `numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens')` return?

```
'12 drummers, XX pipers, five rings, X hens'
```

> 19. What does passing `re.VERBOSE` as the second argument to `re.compile()` allow you to do?

Newlines and comments in the regex will be ignored.

> 20. How would you write a regex that matches a number with commas for every three digits? It must match the following:
> 
> ```
> '42'
> '1,234'
> '6,368,745'
> ```
> 
> but not the following:
> 
> ```
> '12,34,567' (which has only two digits between the commas)
> '1234' (which lacks commas)
> ```

```
\d{0,3}(,\d{3})*
```


> 21. How would you write a regex that matches the full name of someone whose last name is Nakamoto? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
> 
> ```
> 'Satoshi Nakamoto'
> 'Alice Nakamoto'
> 'Robo op Nakamoto'
> ```
> but not the following:
> ```
> 'satoshi Nakamoto' (where the first name is not capitalized)
> 'Mr. Nakamoto' (where the preceding word has a nonletter character)
> 'Nakamoto' (which has no first name)
> 'Satoshi nakamoto' (where Nakamoto is not capitalized)
> ```

```
re.compile(' [A-Z][a-z ]+Nakamoto')
```

> 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
> 
> ```
> 'Alice eats apples.'
> 'Bob pets cats.'
> 'Carol throws baseballs.'
> 'Alice throws Apples.'
> 'BOB EATS CATS.'
> ```
> 
> but not the following:
> 
> ```
> 'Robo op eats apples.'
> 'ALICE THROWS FOOTBALLS.'
> 'Carol eats 7 cats.'
> ```

```
re.compile('(Alice|Bob|Carol) (eats|pets|throws) (apple|cats|baseballs).*\.', re.IGNORECASE)
```