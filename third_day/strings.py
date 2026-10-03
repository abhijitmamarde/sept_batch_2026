name = "manish"

name1 = "abhijit's and my age=\"42\""
name2 = 'abhijit\'s and my age="42"' # escape char --> \ 
name3 = """abhijit's age is "42" """
name4 = '''abhijit's age is "42" '''

print(name1)
print(name2)
print(name3)
print(name4)

# len, 
print(len(name1))
print(name1[0])
print(name1[-1])
print(name1[0:3])
print(name1[::-1])

# this wont work
# TypeError: 'str' object does not support item assignment
# name1[0] = 't'
# print(name1)

s1 = "hello"
print(s1)
print(id(s1))

s1 = s1 + " " + "world"
print(s1)
print(id(s1))

s1 = "hello"
s1 = f"{s1} World!"
print(s1)

l = list(s1)
print(l)

t = tuple(s1)
print(t)

s2 = "".join(l)
print(s2)

l = s1.split(" ")
print(l)
s2 = " ".join(l)
print(s2)

# case related
print("Upper:", s2.upper())
print("lower: ", s2.lower())
print("title: ", s2.title())
print("swapcase: ", s2.swapcase())
print("capitalize: ", s2.capitalize())

data = "aaa bbb ccc ddd eee"
print("ddd" in data)
print("ddD" in data)
print("DDD" in data.upper())

# returns index pos if found OR -1
print(data.find("ddd"))
print(data.find("ddD"))
print(data.find("aaa"))

# index; works as find, but raises ValueError
print(data.index("ddd"))
# print(data.index("ddD")) # ValueError: substring not found

# count
s = "aaa bbb aaa ccc ccc ddd aaa eee ddd"
print(s.count("aaa"))
print(s.count("eee"))
print(s.count("eeD"))

s = "aaa bbb aaa ccc ccc ddd aaa eee ddd"
print(s.replace("aaa", "**AAA**"))

name = "    ABC    "
print(name, len(name))
print(name.strip(), len(name.strip()))
print(name.rstrip(), len(name.rstrip()))
print(name.lstrip(), len(name.lstrip()))

para = """
     

            Hey       
            
            
            You


                 
"""
print(para.strip())


line = "<secret>this is my password</secret>"
print(line.startswith("<secret>"))
print(line.endswith("</secret>"))