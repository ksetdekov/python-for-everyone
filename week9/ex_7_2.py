# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
# fh = open('mbox-short.txt')
total = None
count = None
average = None
for line in fh:
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
print("Average spam confidence:", "{:.12f}".format(average))
