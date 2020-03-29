counts = dict()
names = ['csev', 'cwen', 'csev', 'zquin', 'anna', 'kirill', 'anna']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)
