import math
import random

print(max("hello world&"))
print(min("hello world&"))


def thing():
    print("hello")
    print("fun")


thing()
print("zip")
thing()

# type conversions
print(float(99) / 100)
i = 42
type(i)
f = float(i)
print(f)
type(f)
print(1 + 2 * float(3) / 4 - 5)

sval = "123"
ival = int(sval)
print(type(ival))
print(ival + 1)


def print_lyrics():
    print("im a lumberjack and I'm okay")
    print("I sleep all night and I work all day")


print_lyrics()


# params
def greet(lang):
    if lang == "es":
        return "hola"
    elif lang == "fr":
        return "bonjour"
    else:
        return "hello"


greet('es')


# using return
def greeter():
    return "hello"


print(greeter(), "Kirill")
print(greet("es"), "Chuck")


def addtwo(a, b):
    return a + b


x = addtwo(3, 6)
print(x)

print(math)
ratio = 1000 / 1
decibels = 10 * math.log10(ratio)
print(decibels)

degree = 45


def to_radian(deg):
    return deg / 360.0 * 2 * math.pi


print(math.sin(to_radian(degree)))

# random

for i in range(10):
    # from 0 to 9
    x = random.gauss(0, 1)
    print(x)
    print(i)

for i in range(10):
    x = random.randint(1, 365)
    print(x)

t = range(12)
for i in range(10):
    x = random.choice(t)
    print(x)


# multiple lines from 1
def print_twice(par):
    print(par)
    print(par)


print_twice("spam " * 4)
