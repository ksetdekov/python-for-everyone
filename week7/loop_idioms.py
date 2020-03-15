largest_so_far = -1
print("before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("after", largest_so_far)

# counting
zork = 0
print("before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + 1
    print(zork, thing)
print("after", zork)

# sum
zork = 0
print("before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("after", zork)

# filter
print("before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("large num", value)
print("after")

# search
found = False
print("before", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        break
    print(found, value)
print("after", found)

# min
print("min")
search_list = [9, 41, 12, 3, 74, 15]
smallest_so_far = None
print("before", smallest_so_far)
for the_num in search_list:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)
print("after", smallest_so_far)
