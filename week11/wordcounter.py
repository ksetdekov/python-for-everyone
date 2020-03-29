import string

name = input('enter file')
try:
    handle = open(name)
except FileNotFoundError:
    print('file cannot be opened', name)
    exit()

counts = dict()
for line in handle:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
handle.close()

bigcount = None
bigword = None
for wrd, cnt in counts.items():
    if bigcount is None or cnt > bigcount:
        bigword = wrd
        bigcount = cnt

print('most used word', bigword, 'used', bigcount, 'times')
