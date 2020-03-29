counts = dict()
names = ['csev', 'cwen', 'csev', 'zquin', 'anna', 'kirill', 'anna']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
