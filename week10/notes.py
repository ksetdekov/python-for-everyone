lotto = [2, 13, 34, 51, 88]
print(lotto)
lotto[3] = 999
print(lotto)
# list is changed
# length
print(len(lotto))

# range
print(range(len(lotto)))

# creating a counted loop
friends = ["jo", "glen", "sally"]
for i in range(len(friends)):
    friend = friends[i]
    print("happy new year:", friend)
print("done!")
