fhandle = open("mbox.txt", 'r')
print(fhandle)
stuff = 'hello\nWorld!'
print(stuff)
len(stuff)
count = 0
for cheese in fhandle:
    # print(cheese)
    count = count + 1
print('Line count:', count)

# read all
fhand = open('mbox.txt')
inp = fhand.read()
print('all characters', len(inp))
print(inp[:20])

# read exhausts
fhand = open('mbox.txt')
print(len(fhand.read()))
print(len(fhand.read()))

# searching
fromcount = 0
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        fromcount = fromcount + 1
        print(line)
print(fromcount)

# invert this, this is same result
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)
# in to select lines
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if '@uct.ac.za' not in line:
        continue
    print(line)
