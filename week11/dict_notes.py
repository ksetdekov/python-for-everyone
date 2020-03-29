purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 3
print(purse)

purse = {'money': 112, 'candy': 6, 'tissues': 75}
print(list(purse))
print(purse.keys())
print(purse.values())

for k, v in purse.items():
    print(k, v)

word = 'brontosaurus rex'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
