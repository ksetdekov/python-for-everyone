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