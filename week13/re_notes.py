import re  # regular expression import

hand = open('../files/mbox.txt')
for line in hand:
    line = line.strip()
    if re.search('From:', line):
        print(line)

# same as
for line in hand:
    line = line.strip()
    if line.find('From:') >= 0:
        print(line)

# starting from
for line in hand:
    line = line.strip()
    if re.search('^From:', line):
        print(line)

# same as
for line in hand:
    line = line.strip()
    if line.startswith('From:'):
        print(line)

# wildcard characters
hand = open('../files/mbox.txt')
for line in hand:
    line = line.strip()
    if re.search('^X-DSPAM.*:', line):
        print(line)
hand.close()

# wildcard characters, non-whitespace character and more than 1 time
hand = open('../files/mbox.txt')
for line in hand:
    line = line.strip()
    if re.search('X- \S +:', line):
        print(line)
hand.close()

# matching and extracting data
# re.search() - T/F, re.findall() - get the string

x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)  # get all matching stings in a list

y = re.findall('[AEIOU]+', x)
print(y)

y = re.findall('[aeioy]+', x)
print(y)

# greedy matching
x = 'From: Using the : chareacter'
y = re.findall('^F.+:', x)
print(y)

# non-greedy matching (shortest)
x = 'From: Using the : chareacter'
y = re.findall('^F.+?:', x)
print(y)

# fine-tune string extraction
stringtest = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From (\S+@\S+)', stringtest)  # match all regex, but extract ()
print(y)

# regex extract domain name
stringtest = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)', stringtest)
print(y)
