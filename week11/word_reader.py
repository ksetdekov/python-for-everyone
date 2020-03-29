name = "../files/words.txt"
handle = open(name)

counts = dict()
i = 0
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, i)
        i += 1
handle.close()
print(counts)

print('tasks' in counts)
