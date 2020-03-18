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