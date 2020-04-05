import re

name = input("Enter file:")
if len(name) < 1:
    name = "../files/mbox-short.txt"

fh = open(name)
count = 0
counts = dict()
for line in fh:
    line = line.rstrip()
    time = re.findall('^From .* ([0-9][0-9]):', line)
    if len(time) > 0:
        time = time[0]
        counts[time] = counts.get(time, 0) + 1

fh.close()

TimeList = list()
for k, v in counts.items():
    newtup = (k, v)
    TimeList.append(newtup)

TimeList = sorted(TimeList)
for key, val in TimeList[:]:
    print(key, val)
