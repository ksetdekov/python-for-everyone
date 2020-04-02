import string

fhand = open('../files/romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
# list comprehension
print(sorted([(v, k) for k, v in counts.items()], reverse=True)[:10])
