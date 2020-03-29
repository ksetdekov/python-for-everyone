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
        domain = sender.split('@')[1]
        counts[domain] = counts.get(domain, 0) + 1

fh.close()
highest = None
bigcount = None
for k, v in counts.items():
    if highest is None or v > bigcount:
        highest = k
        bigcount = v
print(highest, counts[highest])
print(counts)
