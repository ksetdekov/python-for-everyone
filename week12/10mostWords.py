fhand = open('../files/romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

WList = list()
for k, v in counts.items():
    newtup = (v, k)
    WList.append(newtup)

WList = sorted(WList, reverse=True)
for val, key in WList[:10]:
    print(key, val)
