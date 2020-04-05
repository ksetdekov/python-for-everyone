import re

handle = open('../files/mbox.txt')
numlist = list()
for lin in handle:
    lin = lin.strip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', lin)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
handle.close()
print('Maximum spam conf.:', max(numlist))
