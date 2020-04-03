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
    if re.search('X-\S+:', line):
        print(line)
hand.close()
