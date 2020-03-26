max_num = None
min_num = None
while True:
    line = input("enter number :")
    if line == "done":
        break
    try:
        num = int(line)
    except ValueError:
        print("Invalid input")
        continue
    if max_num is None:
        max_num = num
        min_num = num
    elif num > max_num:
        max_num = num
    elif num < min_num:
        min_num = num
print("Maximum is", max_num)
print("Minimum is", min_num)
