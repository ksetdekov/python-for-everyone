import re
fhand = open('regex_sum_42.txt')
numbers = list()
for line in fhand:
    linenumbers = re.findall('[0-9]+', line)
    if len(linenumbers) == 0:
        continue
    for num in linenumbers:
        num = int(num)
        numbers.append(num)
# list comprehension
fhand.close()
print(sum(numbers))
