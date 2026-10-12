# d = {}
d = {
    "one": 1,
    "two": 2,
    "aaa": 999,
    "bbb": 9999,
    "ccc": 1000,
    # "zzz": "abc",  # KeyError 'zzz'
}
print(d)
print(type(d))
print(len(d))
print(isinstance(d, dict))

for k, v in d.items():
    print(f"key={k}, value={v}")

print(d["ccc"])
print(d["aaa"])
# print(d["zzz"]) # KeyError 'zzz'

# list
# d[2] = "abc"

# dict
d["aaa"] = "modifed aaa value"
print(d["aaa"])

keys = list(d.keys())
print(f"All Keys are: {keys}")

values = tuple(d.values())
print(f"All Values are: {values}")

keys = (1, 2, 3)
values = [11, 12, 13]
d2 = dict(zip(keys, values))
print(d2)
print(type(d2))
print(len(d2))
print(isinstance(d2, dict))


marks = {
    "abhi": 97,
    "sagar": 89,
    "manish": 91
}

# summation of all marks
# total_marks = sum([97, 89, 91])
total_marks = sum(marks.values())
print(f"Sum of all students marks is: {total_marks}")


marks2 = {
    "abhi": [97, 89, 88],
    "sagar": [89, 81, 82],
    "manish": [91, 99, 98],
}

# summation of all marks
total_marks = 0
for k, v in marks2.items():
    total_marks += sum(v)
print(f"Sum of all students marks is: {total_marks}")

# Assignment
# 1. Verify the sum is correct
# 2. Print average of each student
# 3. Use the values in tuple and see if any changes required in program or not


d3 = {
    "aaa": 1,
    "bbb": 2,
    3: "ccc",
    "aaa": 100, # basically overwridding ealrier define val of "aaa": 1
    "zzz": (500, 600)  # 2 values for key zzz
}

# a = 1
# b = 2
# c = 3
# # ... after 100 lines
# a = 100
# print(a)

print(d3)
print(d3[3]) # thids is not index pos, it is checking value at key: 3
print(d3["aaa"])



#########################

d4 = {"aaa": 99}
d4["aaa"] = 1
d4["bbb"] = 2
d4["ccc"] = 3
print(d4)

print(d4["bbb"])
del(d4["bbb"]) # bbb key is deleted, no more existing
print(d4)
# print(d4["bbb"]) # KeyError: 'bbb'

# if a key exists or not!
if "bbb" in d4:
    print("bbb key exists!")
else:
    print("bbb key does not exists!")

if "bbb" not in d4:
    print("bbb key does not exists!")
else:
    print("bbb key exists!")


sum_values = d4["aaa"] + d4.get("bbb", 0) + d4["ccc"]
print(f"Sum is: {sum_values}")
