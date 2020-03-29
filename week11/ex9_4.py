import operator

name = input("Enter file:")
if len(name) < 1:
    name = "../files/mbox-short.txt"

fh = open(name)
count = 0
counts = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    line_words = line.rstrip().split()
    if line_words[0] == 'From':
        sender = (line_words[1])
        counts[sender] = counts.get(sender, 0) + 1

fh.close()
highest = max(counts.items(), key=operator.itemgetter(1))[0]
print(highest, counts[highest])
