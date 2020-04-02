x = ('glenn', 'sally', 'joseph')
print(x[2])
y = (1, 9, 2)  # tuple has these braces
print(y)
print(max(y))
for i in y:
    print(i)

list_l = list()
print(dir(list_l))

t = tuple()
print(dir(t))
# count and index

# simultaneous assignment - like R
(a, b) = (99, 98)
print(a)
(c, d) = (x, y)
print(c)

# dictionary is a list of tuples

# compare tuples
# element by element comparison
print((0, 1, 2) < (5, 1, 2))
print((0, 1, 2000) < (0, 3, 4))

# sorting list of tuples
s = {'a': 10, 'c': 22, 'b': 1}
print(s.items())
print(sorted(s.items()))  # sort by the key

# looping by key order
t = sorted(s.items())
print(t)
for k, v in sorted(s.items()):
    print(k, v)

# sort by value
tmp = list()  # list
for k, v in s.items():
    tmp.append((v, k))  # list of tuples
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)

t = ('A',) + x[1:]
print(t)  # replace 1 tuple with other

# switch variable content
a = 5
b = 'John'
a, b = b, a
print(a, b)
adr = 'test@email.com'
uname, domanain = adr.split('@')
print(uname)
print(domanain)

# composite keys
directory = dict()

directory['last', 'first'] = 100
directory['setdekov', 'john'] = 123213
for last, first in directory:
    print(first, last, directory[last, first])
