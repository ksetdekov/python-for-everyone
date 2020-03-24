numlist = list()
while True:
    inp = input('enter a num:')
    if inp == 'done':
        break
    try:
        value = float(inp)
    except ValueError:
        print('non numeric')
        continue
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('average is:', average)
