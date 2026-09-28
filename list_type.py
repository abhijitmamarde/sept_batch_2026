l1 = [1, 2, 3]
l2 = ['aaaa', 'bbbb', 'cccc']
l3 = ['aaaa', 1, 'bbbb', 3, 'cccc', None, True]

print(l1)
print(l2)
print(l3)

# Using, array indexing starts from 0
# always a positive and valid number
print(l1[0]) #--> 1
print(l1[1]) #--> 2
print(l1[2]) #--> 3

print(l2[0])
print(l2[1])
print(l2[2])

print(l3[4])

# last value
# len
print(len(l1))
print(len(l2))
print(len(l3))

print(l1[len(l1)-1])
print(l2[len(l2)-1])
print(l3[len(l3)-1])

# this wont work, as len gives abosulte number of values in list; index pos is 1 less than that
# print(l3[len(l3)]) # IndexError: list index out of range

# Slice
# [from:until] - starts from `from`, one less than `until` 
# l3 = ['aaaa', 1, 'bbbb', 3, 'cccc', None, True]
print(l3[1:3]) # [1, 'bbbb']
print(l3[1:2]) # [1]

# gives me full objects
print(l3[0:7])
print(l3[0:len(l3)])

days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# Days of Weekday
print(days_of_week[3-1:5])
print(days_of_week[3-1:len(days_of_week)-2])

# Slice
# [from:until] - from and until both are optional; they have defaults of from:0, unitl: len
print(l3[0:len(l3)])
print(l3[:len(l3)])
print(l3[0:])
print(l3[:])

# shortcut for duplicating a list
l4 = l3[:]
print(l4)

# [from:until] can also have negative index positions
print(l3[1:-2])
print(l3[1:len(l3)-2])

# [from:until:step] by def, step is 1
print(l3[0:7])
print(l3[0:7:1])
print(l3[0:7:2])
print(l3[0:7:3])

print(l3)
print(l3[::-1])
print(l3[::-2])
