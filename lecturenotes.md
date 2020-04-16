# week 3
## writing paragraphs of code

`=` - assignment statement

`x = x + 1` - assignment statement with operator

### reserved words
cant have variables with this:

`['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']`

### python script!

Do not type to much into console.

### constants
* cant use reserved words as var names
* start with a letter or underscore
* consist of letters, numbers and underscores
* case sensitive

## expression
* `**` power
* `%` remainder

**Order**:
1. parenthesis
2. power
3. multiplication
4. addition 
5. left to right

Variables, literals and constants have a type.

`+` adds numbers and concatenates for string

```
type(1)
<class 'int'>

type("text")
<class 'str'>
```

**Do not use float for money!**

In Python 2 integer division was integer, not float and left only the integer part.

### user input
`input` returns a string

# week 5
## conditional statements
indent by 4 spaces
indenting is **required**
turn of tabs
### comparison operators
```
!= не 
== равно
```

### try except structure (catch traceback)
if try works - except is skipped

if try fails - jump to the except section

# week 6

**store and reuse**

def.

```python
def thing():
    print("hello")
    print("fun")

thing()
```

STRING CONVERSIONS

```python
sval = "123"
ival = int(sval)
print(type(ival))
print(ival+1)
```

**using return**

```python
def greet(lang):
    if lang == "es":
        return "hola"
    elif lang == "fr":
        return "bonjour"
    else:
        return "hello"


greet('es')


# using return
def greeter():
    return "hello"


print(greeter(), "Kirill")
print(greet("es"), "Chuck")
```

**multi params**

```python
def addtwo(a, b):
    return a + b


x = addtwo(3, 6)
print(x)
```

**multiple runs**

# week 7 Using loops and iterations
## breaking out of loop

this is using `break`
```python
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("done")
```

finishing iteration
```python
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("done")
```

## definite loop
```python
for i in [5, 4, 3, 2, 1]:
    print(i)
print("blastoff")
```

## loop idioms
### largest
```python
largest_so_far = -1
print("before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("after", largest_so_far)
```

* count
* sum
* filter
* search with boolean
* min

```python
# counting
zork = 0
print("before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("after", zork)

# sum
zork = 0
print("before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("after", zork)

# filter
print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("large num", value)
print("after")

# search
found = False
print("before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print("after", found)

# min
print("min")
search_list = [9, 41, 12, 3, 74, 15]
smallest_so_far = None
print("before", smallest_so_far)
for the_num in search_list:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("after", smallest_so_far)
```

### is and is not
* `is` operator
* the same as
* similar but stronger than `==`
* `is not` is an inversion

# python data structures
## strings
### looking inside strings
```python
fruit = "banana"
print(fruit[10])
```
we get `IndexError`

can have better loops over strings
```python
fruit = "banana"
for letters in fruit:
    print(letters)
```

### slicing strings
```python
s = "Monty Python"
print(s[0:4])
# output Mont
```
Не ужно указывать оба конца
```python
s = "Monty Python"
print(s[:2])
print(s[8:])
print(s[:])
```
Можно проверять наличие через `in`
```python
fruit = "banana"
if 'nan' in fruit:
    print("found \"nan\"")
```

### format operator
The format operator, `%` allows us to construct strings, replacing parts of the strings with the data stored in variables. 
When applied to integers, `%` is the modulus operator. But when the first operand is a string, `%` is the format operator.`%`
### showing what is in a line
```python
s = '1 2\t 3\n 4'
print(s)
# 1 2	 3
#  4
print(repr(s))
# '1 2\t 3\n 4'
```
# week 10 lists
algorithms 
* set of rules

data structures
* way to organize data in a computer

**list is a kind of a collection**
```python
friends = ['kevin', 'mike']
list_of_lists = [1,[5,6],10]
emptylist = []
for i in list_of_lists:
    print(i)
# 1
# [5, 6]
# 10
```

**lists are mutable, can be changed**

# week 9, files
## opening and reading them

**fhandle**
```python
fhandle = open('week9/mbox.txt')
print(fhandle)
```

**iterating over lines**
```python
fhandle = open('week9/mbox.txt')
count = 0
for cheese in fhandle:
    print(cheese)
    count = count + 1
```

**useful  to strip new line character**
```python
fhand = open('week9/mbox.txt')
for line in fhand:
    line = line.rstrip()
    print(line)
```

# week 11 dictionaries
type of a collection (many things in one)

dictionary is an an associative array
* no order
* have index
* use keys instead of location (in lists)
* shown  in {}

** can loop over 2 iteration variables at a time*
```python
purse = {'money': 112, 'candy': 6, 'tissues': 75}

for a, b in purse.items():
    print(a, b)

# money 112
# candy 6
# tissues 75
```

# tuples are like lists

like a list with index starting at 0

Tuples are "immutable"
Lists and tuples are immutable. Lists are.
 
Can do much less
 ```python
t = tuple()
print(dir(t))
# count and index
```

## list comprehension
```python
# list comprehension
purse = {'money': 112, 'candy': 6, 'tissues': 75}
print(sorted([(v, k) for k, v in purse.items()], reverse=True)[:10])
```
works in a way, like we had `for all members in a dict, create a tuple `

# regular expressions


<img src="https://imgs.xkcd.com/comics/regular_expressions.png"
     alt="Regular_expression, https://xkcd.com/208/ "
     style="float: left; margin-right: 10px;" />

### Python Regular Expression Quick Guide
https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

howto for python https://docs.python.org/3/howto/regex.html
```
^        Matches the beginning of a line
$        Matches the end of the line
.        Matches any character
\s       Matches whitespace
\S       Matches any non-whitespace character
*        Repeats a character zero or more times
*?       Repeats a character zero or more times (non-greedy)
+        Repeats a character one or more times
+?       Repeats a character one or more times (non-greedy)
[aeiou]  Matches a single character in the listed set
[^XYZ]   Matches a single character not in the listed set
[a-z0-9] The set of characters can include a range
(        Indicates where string extraction is to start
)        Indicates where string extraction is to end
[^ ]     Match non-blank character, ^ is like not
\        Escape character
```

##  matching and extracting data
`re.search()` - T/F, 
`re.findall()` - get the string

```python
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)  # get all matching stings in a list
```

## warning: greedy matching
\* and + push outward both direction to find the biggest match

## non-greedy matching (shortest)
```python
import re
x = 'From: Using the : chareacter'
y = re.findall('^F.+?:', x)
print(y)
```

## extract only part in ()
```python
import re
stringtest = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', stringtest)  # match all regex, but extract ()
print(y)
```

### using escape to match tech characters
```python
import re
x = 'we just got $10.123 and $0.001 for food'
y = re.findall('\$[0-9.]+', x)
print(y)
# ['$10.123', '$0.001']
```

# web data week 4
UTF-8 has 1 to 4 byte in character representation

Python 3 - all strings in Unicode

# scraping web pages
web page scraping

**Beautiful soup** - good solution

# data on the web
XML and JSON - formats for data between applications
these are serialization formats for data transmission
