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

serialization / de-serialization - converting data in one program into a common format tat can be stored and/or 
transmitted between systems in a programming language-independent manner


## xml basics

* start tag
* end tag
* text content
* attributes - always on start tag. key-value pair
* self closing tags

## XML schema
XML document + XML Schema Contract - sent to XML Validator for Validation

## JSON - JavaScript Object Notation
XML still used - JSON  is very popular.

JSON - data as nested "lists" and "dictionaries"

# object oriented programming

object - bit of self-contained Code and Data

## definitions

* **class** - template
* **method** or message - a defined capability of a class
* **field** or attribute - a bit of data in a class
* **object** or Instance - a particular instance of a class

Class - template for making things
Instance - this is a particular object (real things)
Method - defined in a class, part of an object

```python
x = 'abc'
type(x)
type(2.4)
type(2)
z = list()
type(z)
y = dict()
type(y)
```

## object life cycle

* created use and discarded
* constructor - moment of creation - used a lot
* destructor - moment of destruction

## inheretence
parent class - then we create a child class that inherits a parent class attributes


# relational databases

https://www.sqlitebrowser.org

https://en.wikipedia.org/wiki/Relational_database

## terminilogy
* database - contains tables
* relation (table) - contains tuples and attributes
* tuple (row) - set of fields that generally represent an "object"
* attributes (columns, fields) - one of the many elements of data corresponding to the object represented by the row

## SQL
* **Structured Query Language** - language we use to issue commands to the database
    * **C**reate a table
    * **R**etrieve data
    * insert data
    * **U**pdate
    * **D**elete data

<img src="files/DB structure.PNG"
     alt="DB structure"
     style="float: left; margin-right: 10px;" />
     
 ### First DB

```iso92-sql
CREATE TABLE Users(
	name VARCHAR(128),
	email VARCHAR(128)
)
```

#### SQL Insert
```iso92-sql
INSERT INTO Users (name, email) VALUES ('Kristin', 'kf@umich.edu')
```

#### Delete row
```iso92-sql
DELETE FROM Users WHERE email='ted@umich.edu'
```

#### Update
```iso92-sql
UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'
```

#### Select
```iso92-sql
SELECT * FROM Users
```
```iso92-sql
SELECT * FROM Users WHERE email='csev@umich.edu'
```

#### Sort
```iso92-sql
SELECT * FROM Users ORDER BY email
SELECT * FROM Users ORDER BY name
```

# week 19 data models
## Designing a data model

* draw a picture of data objects for your application, figure out how to represent them as objects and relations
* basic rule = don't put same string twice - use a relationship instead
* when there is one thing in the real world, there should be one copy of that thing in the DB

### Let's build music library app
**is it an object or an attribute of a thing?**
* where to start? - what is the most important thing of the app
    * track - this is a track management app
    
* identify keys
    * primary key - id of the rows in a table
    * logical key - mark a column, that might be used for retrieval (name)
    * foreign key - album_id in a table of tracks (origin of an arrow from track table)

Work from outside in
 
```iso92-sql
CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"Name"	TEXT
)

CREATE TABLE "Genre" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    "name" TEXT)

CREATE TABLE "Album" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    artist_id INTEGER,
    "title" TEXT)

CREATE TABLE "Track" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER,
    rating INTEGER,
    "title" TEXT,
    "count" INTEGER)
```


Entering data, going from outward most layer
```iso92-sql
INSERT INTO Artist (name) VALUES ('Led Zepplin');
INSERT INTO Artist (name) VALUES ('AC/DC');
INSERT INTO Genre (name) VALUES ('Rock') ;
INSERT INTO Genre (name) VALUES ('Metal')
```

Album data has to be related to the artist:
```iso92-sql
INSERT INTO Album (title, artist_id) VALUES ('Who Made Who', 2);
INSERT INTO Album (title, artist_id) VALUES ('IV', 1);
```
Tracks
```iso92-sql
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Black Dog', 5, 297, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Stairway', 5, 482, 0, 2, 1) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('About to Rock', 5, 313, 0, 1, 2) ;
INSERT INTO Track (title, rating, len, count, album_id, genre_id) 
    VALUES ('Who Made Who', 5, 207, 0, 1, 2) ;
```

## Joining data

```iso92-sql
SELECT Album.title, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
```

the source of the connection is:
```iso92-sql
SELECT Album.title, Album.artist_id, Artist.id, Artist.name FROM Album JOIN Artist ON Album.artist_id = Artist.id
```

title and genre
```iso92-sql
SELECT Track.title, Genre.name FROM Track JOIN Genre 
    ON Track.genre_id = Genre.id
```

join without an on clause gives all possible combinations

This give a Track, Artist, Album, Genre result
```iso92-sql
SELECT Track.title, Artist.name, Album.title, Genre.name 
FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.id AND Track.album_id = Album.id 
    AND Album.artist_id = Artist.id
```

### some useful SQL
`INSERT OR REPLACE` - update if already there

`INSERT OR IGNORE` - don't blow up

retrieve data from tracks.py:
```iso92-sql
SELECT Track.title, Album.title, Artist.name 
FROM Track JOIN Album JOIN Artist 
on track.album_id = Album.id and Album.artist_id= Artist.id
```

# Many to many realtionship

* books and authors
    * can have many books
    * a book can have many authors

**junction table** 

* course table
    * id
    * title
* user table
    * id
    * name
    * email
* member table
    * user_id
    * course_id
    * role
    
```
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE,
    email  TEXT
) ;

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
) ;

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
	role        INTEGER,
    PRIMARY KEY (user_id, course_id)
) ;
```

#### Using data from handouts:

https://www.py4e.com/lectures3/Pythonlearn-15-Database-Handout.txt

# Multi-Step Data Analysis

1. gather data from Data source to DB
2. clean/Process (from DB to cleanDB)
3. Vizualize
4. Analyse

This is more complex but not data mining yet.

Read this for more:

* hadoop
* spark apache
* redshift amazon
* pentaho community

# pagerank running

info on the origin of google **The Anatomy of a Large-Scale Hypertextual Web Search Engine**

http://infolab.stanford.edu/~backrub/google.html

1. spider.py - spider
2. spider.sqlite - db
3. spreset - clears data in 2.
4. sprank - ranking algorithm on 2. data
5. spdump - dumps content of 2.
6. spjson - creates from 2. data for 7.
7. force.js - vizualizes
8. force.html - webpage with wiz