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

print(s[:2])
print(s[8:])
print(s[:])
