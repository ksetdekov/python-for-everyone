h = input("Enter Hours:")
w = input("enter rate")
try:
    w = float(w)
    h = float(h)
except ValueError:
    print("enter numeric input")
    quit()
if h > 40:
    pay = 40 * w + (h - 40) * 1.5 * w
else:
    pay = w * h
print(pay)
