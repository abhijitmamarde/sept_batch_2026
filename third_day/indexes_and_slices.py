l3 = ['aaaa', 1, 'bbbb', 3, 'cccc', None, True]

print(l3[0])
print(l3[6])
print(l3[len(l3)-1])

# IndexError: list index out of range
# print(l3[7])

# negative works as slices... len(l3) - x
print(l3[-1])
print(l3[-7])

# IndexError: list index out of range
# print(l3[-8])


# slice - from, to, step
# shortcut for copying the list
print("============")
l = l3[::]
print(l)
print(f"id of l3 is: {id(l3)}")
print(f"id of l is: {id(l)}")

l3[0] = 1000
print(l3)
print(l)

# shortcut for copying the list elements in reverse order
l = l3[::-1]
print(l)

# this just creates a new reference / variable pointing to same list as of l3
l2 = l3
print(l3)
print(l2)
print(f"id of l3 is: {id(l3)}")
print(f"id of l2 is: {id(l2)}")

# if we change anything in l3, l2 is impacted as well
l3[0] = 5000
print(l3)
print(l2)


a = 1
b = a
a = a + 2
print(a, b)
print(id(a), id(b))
