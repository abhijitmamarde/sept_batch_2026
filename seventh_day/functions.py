from types import FunctionType

def mysum(n1=0, n2=0):
    return n1 + n2

print(mysum(1, 2))
print(mysum(1))
print(mysum())

# wwe are not calling / triggering the func
# 
print(mysum)
print(type(mysum))

print(isinstance(mysum, FunctionType))
