name = input('enter file')
handle = open(name)

counts = dict()
for line in handle:
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
