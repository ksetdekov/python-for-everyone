import math

fruit = "banana"
letter = fruit[1]
print(letter)
x = 3
w = fruit[x - 1]
print(w)

print("all positions")
for i in range(6):
    print(fruit[i])

try:
    print(fruit[10])
except IndexError:
    print("index error, out of bounds")

# len
print("length", len(fruit))

# loop over string
index = 0
while index < len(fruit):
    x = fruit[index]
    print(index, x)
    index = index + 1

# better loop
for letters in fruit:
    print(letters)

# word count
word = fruit
count = None
for letter in word:
    if count is None:
        count = 0
    elif letter == "a":
        count = count + 1
print(count)

# slicing
s = "Monty Python"
print(s[0:4])
# output Mont
print(s[6:100])
# output Python
try:
    print(s[6:(100 * math.pi)])
except TypeError:
    print("TypeError")

# TypeError: slice indices must be integers or None or have an __index__ method
# selecting part of string
print(s[:2])
print(s[8:])
print(s[:])

# concatenation
strA = "Hello"
strB = strA + "There"
print(strB)
c = strA + " " + "There"
print(c)

# logical
fruit = "banana"
if 'nan' in fruit:
    print("found \"nan\"")

# comparison
word = "abba"
if word == 'banana':
    print('this is banana')
if word < 'banana':
    print('your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('your word, ' + word + ', comes after banana.')
else:
    print('all right, bananas')

# string library
greet = "Hello Bob"
zap = greet.lower()
print(zap)
print(greet)
print('Hi there'.lower())

stuff = 'hello world'
print('J' + stuff[1:])
print(type(stuff))
print(dir(stuff))

# bunch of them
stufflong = "this is a riDiculously long string"
print(stuff.capitalize())
print(stuff.center(21, '_'))
print(stufflong.center(21, '_'))

print(stuff.endswith('world'))
print(stufflong.endswith('world'))

print(stuff.find('world'))
print(stufflong.find('world'))  # -1 if no

print(stuff.lstrip('h'))
print(stuff.rstrip('d'))
print(stuff.center(21, '_').strip('_'))
print('   hello bobs    '.strip())

print(stuff.replace('o', '0'))
print(stufflong.replace(' ', ' fucking '))

print(stufflong.lower())
print(stufflong.upper())

# practice
inputstring = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = inputstring.find('@')
print(atpos)
sppos = inputstring.find(' ', atpos)
print(sppos)
host = inputstring[atpos + 1:sppos]
print(host)

# format
camels = 42
print('%d' % camels)
print('I have spotted %d camels.' % camels)

print('In %d years I have spotted %g %s.' % (3, 0.1, 'camels'))
