l = ['aaaa', 1, 'bbbb', 3, 'cccc', None, True]
t = ('aaaa', 1, 'bbbb', 3, 'cccc', None, True)

# list can be modified, tuples once created can not be modified.
print(len(l))
print(len(t))

print(l[0])
print(t[0])

print(l[6])
print(t[6])

print(l[-1])
print(t[-1])

# Slices also works same... 
print(l[0:3])
print(t[0:3])

print(l[::-1])
print(t[::-1])

l[0] = 9000
# TypeError: 'tuple' object does not support item assignment
# t[0] = 9000 # this will fail


# list to tuple and vice-versa
t2 = tuple(l)
l2 = list(t)
print(t2)
print(type(t2))
print(l2)
print(type(l2))
