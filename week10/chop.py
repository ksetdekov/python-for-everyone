lotto = [2, 13, 34, 51, 88]
print(lotto)


def chop(t):
    del t[0]
    del t[len(t) - 1]


chop(lotto)
print(lotto)

lotto = [2, 13, 34, 51, 88]
print(lotto)


def middle(t):
    return t[1:len(t) - 1]


print(middle(lotto))
