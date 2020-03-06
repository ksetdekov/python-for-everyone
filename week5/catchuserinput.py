raw = input("enter number:")
try:
    ival = int(raw)
except ValueError:
    ival = -1
if ival > 0:
    print("fine")
else:
    print("NaN")
