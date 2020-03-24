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

# adding lists
b = ['1', '2', '3']
c = b + friends
print(c)

# slicing
# up to but not including 3
print(lotto[:3])

# list methods
x = list()
print(type(x))
print(dir(x))

# building from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# in and not in
print(9 in stuff)
print(99 in stuff)
print('names' not in stuff)

# lists are in order
print(friends)
friends.sort()
print(friends)
print(friends[1])

# list functions
print(len(lotto))
print(max(lotto))
print(min(lotto))
print(sum(lotto))
print(sum(lotto) / len(lotto))
