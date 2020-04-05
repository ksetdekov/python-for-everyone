import re
file = '../files/mbox.txt'
regex = input('Enter a regular expression: ')
fhand = open(file)
count = 0
for line in fhand:
    if re.search(regex, line):
        count += 1
fhand.close()
print(file, 'had', count, 'lines that matched', regex)
