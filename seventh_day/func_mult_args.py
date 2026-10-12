# variable number of args
def mycalc(n1, n2, n3, n4=0, n5=0):
    # return multiple values
    return n1 + n2 + n3 + n4 + n5

print(mycalc(1, 2, 3))
print(mycalc(1, 2, 3, 4))
print(mycalc(1, 2, 3, 4, 5))

def new_mycalc(*args, **kwargs):
    print(f"Args are: {args}")
    print(f"Type of Args is: {type(args)}")
    print(f"KWArgs are: {kwargs}")
    print(f"Type of KWArgs is: {type(kwargs)}")

    # Assignment:
    # 1. Return subtractions, multiplications as well
    return sum(args)

print(new_mycalc())
print(new_mycalc(1))
print(new_mycalc(1, 2))
print(new_mycalc(1, 2, 3))
print(new_mycalc(1, 2, 3, 4))
print(new_mycalc(1, 2, 3, 4.5))

args = (1, 2, 3, 4)
sum_values = 0
for i in range(len(args)+1):
    sum_values = sum_values+i
print(f"Sum is: {sum_values}")

print(f"Sum is: {sum(args)}")

# def new_mycalc(n1, n2):
#     ...

# positional arg calling
new_mycalc(1, 2)

# # keywaord arg calling
print("==================== 1")
new_mycalc(n1=1, n2=2)
print("==================== 2")
new_mycalc(n2=1, n1=2)