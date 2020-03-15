total = None
count = None
average = None
while True:
    line = input("enter number :")
    if line == "done":
        break
    try:
        num = int(line)
    except ValueError:
        print("Invalid input")
        continue
    if total is None:
        total = num
        count = 1
        average = num
    else:
        total = total + num
        count = count + 1
        average = total / count
print(total, count, average)
