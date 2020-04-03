import string

name = input("Enter file:")
if len(name) < 1:
    name = '../files/romeo-full.txt'

ValidLetters = string.ascii_letters[:26]
i = 0
fhand = open('../files/romeo-full.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    for letter in line:
        if letter in ValidLetters:
            counts[letter] = counts.get(letter, 0) + 1
# list comprehension
fhand.close()
LetterHist = sorted([(v, k) for k, v in counts.items()], reverse=True)
for k, v in LetterHist:
    print(v, k)
