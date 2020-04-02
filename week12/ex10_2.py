name = input("Enter file:")
if len(name) < 1:
    name = "../files/mbox-short.txt"

fh = open(name)
count = 0
counts = dict()
for line in fh:
    if not line.startswith("From "):
        continue
    line_words = line.rstrip().split()
    if line_words[0] == 'From':
        time = (line_words[5])[:2]
        counts[time] = counts.get(time, 0) + 1

fh.close()

TimeList = list()
for k, v in counts.items():
    newtup = (k, v)
    TimeList.append(newtup)

TimeList = sorted(TimeList)
for key, val in TimeList[:]:
    print(key, val)
