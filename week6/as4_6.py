def computepay(hours, wage):
    if hours > 40:
        pay = 40 * wage + (hours - 40) * 1.5 * wage
    else:
        pay = wage * hours
    return pay


h = input("Enter Hours:")
w = input("enter rate")
try:
    w = float(w)
    h = float(h)
except ValueError:
    print("enter numeric input")
    quit()

p = computepay(h, w)
print("Pay", p)
