from functools import reduce

ages = [17, 18, 21, 50, 120, 9]

# filters - builtin funcs which is used to filter out the list of elements on spec cond

# i need this, after the filter (>= 18 and <= 100)
# ages = [18, 21, 50]

# manual logic for the required filter operation
ages = [17, 18, 21, 50, 120, 9]

filtered_ages = []
for age in ages:
    if (age >= 18) and (age <= 100):
        filtered_ages.append(age)
print(filtered_ages)

# instead we could use filter func like below:
# using lambda - nameless function
filtered_ages = list(filter(lambda age: (age >= 18) and (age <= 100), ages))
print(filtered_ages)
print(type(filtered_ages))

# using custom filter func
def my_age_filter(age):
    if (age >= 18) and (age <= 100):
        return True
    return False

filtered_ages = list(filter(my_age_filter, ages))
print(filtered_ages)
print(type(filtered_ages))

data = [
    {
        "name": "aaa",
        "age": 17,
        "is_indian": True,
    },
    {
        "name": "bbb",
        "age": 18,
        "is_indian": True,
    },
    {
        "name": "ccc",
        "age": 18,
        "is_indian": False,
    },
    {
        "name": "ddd",
        "age": 17,
        "is_indian": True,
    }
]

# using custom filter func
def my_custom_age_filter(d):
    if (d["age"] >= 18) and (d["age"] <= 100) and (d["is_indian"] is True):
        return True
    return False

recs = list(filter(my_custom_age_filter, data))
print(recs)
print(type(recs))

# map
# map / call the function for all elements of an list/tuple
l1 = [1, 2, 3, 4, 5]
res = []
for i in l1:
    res.append(i*2)
print(res)

# using map
def mul_by_2(i):
    return i*2

res = list(map(mul_by_2, l1))
print(res)

res = list(map(lambda i: i*2, l1))
print(res)

# reduce
# its an algo which reduces multiple counts of elements to less than the original

l1 = [1, 7, 2, 6, 5]
print(sum(l1))

result = reduce(lambda x, y: x*2 + y*2, l1)
print(result)

def my_custom_reduce_algo(x, y):
    return x*2 + y*2

result = reduce(my_custom_reduce_algo, l1)
print(result)