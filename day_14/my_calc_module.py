def myadd(n1, n2):
    res = n1 + n2
    print(f"Add of {n1} and {n2} is: {res}")
    return res

def mysub(n1, n2):
    res = n1 - n2
    print(f"Sub of {n1} and {n2} is: {res}")
    return res

def myabssub(n1, n2):
    res = 0
    if n1 > n2:
        res = n1 - n2
    else:
        res = n2 - n1
    print(f"ABS sub of {n1} and {n2} is: {res}")
    return res

