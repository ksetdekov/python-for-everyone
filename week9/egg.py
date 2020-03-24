# Use the file name mbox-short.txt as the file name
import os

fname = input("Enter file name: ")

if os.path.isfile(fname):
    total = None
    count = None
    average = None

    fname = open(fname)
    for line in fname:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        line = line.rstrip()
        num = float(line[(line.index(': ') + 2):])
        if total is None:
            total = num
            count = 1
            average = num
        else:
            total = total + num
            count = count + 1
            average = total / count
    if count is None:
        print('spam index', count)
    else:
        print("Average spam confidence:", "{:.12f}".format(average))
elif fname == 'nanahaha':
    print('PWND', fname.upper(), 'to you!')
else:
    print('incorrect fname')
    quit()
