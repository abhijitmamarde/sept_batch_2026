def myadd_v2(n1, n2):
    res = n1 + n2
    print(f"V2. Add of {n1} and {n2} is: {res}")
    return res

def mysub_v2(n1, n2):
    res = n1 - n2
    print(f"V2. Sub of {n1} and {n2} is: {res}")
    return res

def myabssub_v2(n1, n2):
    res = 0
    if n1 > n2:
        res = n1 - n2
    else:
        res = n2 - n1
    print(f"V2. ABS sub of {n1} and {n2} is: {res}")
    return res

