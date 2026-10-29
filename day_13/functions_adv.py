# Formal and Act args
# formal -> during func calling, formal parameters
# actual args -> once func is called, what we could use in the funct, actual parameters 

def mysub(n1, n2):
    print(f"n1 is: {n1}, n2 is: {n2}")
    return n1 - n2

print(mysub(5, 3))

n1 = 10
n2 = 30
print(mysub(n2, n1)) # --> Pos arg

print(mysub(n2=n1, n1=n2))  # --> Keyword arg

