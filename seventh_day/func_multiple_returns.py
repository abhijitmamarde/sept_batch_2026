def mycalc(n1=0, n2=0):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

print(mycalc(5, 2))

sum = mycalc(5, 2)
print(sum)
print(type(sum))
print(isinstance(sum, tuple))

print(f"Multiplication result is: {sum[2]}")
print(f"Total results are: {len(sum)}")

# Assignment: hint for 2-5 use slices
# 1. Print for sum, div, sub
# 2. Print - (add, sub)
# 3. Print - (mul, div)
# 4. Print - (div, mul)
# 5. Print - (div, mul, sub, add)
