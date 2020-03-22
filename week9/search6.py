fname = input('Enter the file name: ')
fhand = None
try:
    fhand = open(fname)
except FileNotFoundError:
    print('file cannot be opened', fname)
    quit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('Threre were', count, 'subject lines in', fname)
