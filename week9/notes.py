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

fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except FileNotFoundError:
    print('file cannot be opened', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('Threre were', count, 'subject lines in', fname)
