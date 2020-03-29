numbers = list()
while True:
    line = input("enter number :")
    if line == "done":
        break
    try:
        num = int(line)
    except ValueError:
        print("Invalid input")
        continue
    numbers.append(num)
try:
    max_num = max(numbers)
    min_num = min(numbers)
except ValueError:
    max_num = None
    min_num = None
print("Maximum is", max_num)
print("Minimum is", min_num)
