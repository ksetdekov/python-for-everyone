fhandle = open("mbox.txt", 'r')
print(fhandle)
stuff = 'hello\nWorld!'
print(stuff)
len(stuff)

# using repr
s = '1 2\t 3\n 4'
print(s)
# 1 2	 3
#  4
print(repr(s))
# '1 2\t 3\n 4'
