import random

n = random.randint(1, 100)
while n > 0:
    print(n)
    n = n - 1
print("blastoff")
print(n)

# break
while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("done")

# finishing iteration
while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("done")

# for loop
for i in [5, 4, 3, 2, 1]:
    print(i)
print("blastoff")

friends = ["jo", "glen", "sally"]
for friend in friends:
    print("happy new year:", friend)
print("done!")
