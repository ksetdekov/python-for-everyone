txt = 'but soft what light is younder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

res = list()
for length, wrd in t:
    res.append(wrd)

print(res)
