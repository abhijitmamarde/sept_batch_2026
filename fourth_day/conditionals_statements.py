name = "ABC"
age = 17


# >, >=, <, <=
# ==, !=

# and, or, not

if age >= 18:
    print(f"{name} is able to vote!")
    print("Another line 1")
    print("Another line 2")
    print("Another line 3")
    print("Another line 4")
    print("Another line 5")
    print("Another line 6")
else:
    print(f"{name} could not vote for now!")
    print("Another line for no vote 1")
    print("Another line for no vote 2")
    print("Another line for no vote 3")
    print("Another line for no vote 4")
    print("Another line for no vote 5")
    print("Another line for no vote 6")


# if-elif-else
# if elif tree / descision tree

marks = 20
grade = "NA"

if marks >= 90:
    grade = "A+"
elif marks >= 85:
    grade = "A"
elif marks >= 65:
    grade = "B"
elif marks >= 55:
    grade = "C"
else:
    grade = "F"

print(f"{name}  marks are: {marks} and grade is: {grade}")

############

role = "admin"
passwd = "admin1"

if role == "admin":
    if passwd == "admin":
        print("1> Elevated role access granted!")
    else:
        print("1.1> Normal user access given")
else:
    print("1.2> Normal user access given")

if (role == "admin") and (passwd == "admin"):
        print("2> Elevated role access granted!")
else:
    print("2> Normal user access given")

###

role = "admin"
username = "admin"
passwd = "admin123"

if (role == "admin") or ((username == "admin") and (passwd == "admin123")):
    print("User role or username and passwrd cond is valid, acess granted!")
else:
    print("User role or username and passwrd cond is in-valid, acess not granted!")


# not - valid username and password, but the role is not support
role = "admin"  # "support"
username = "admin"
passwd = "admin123"

if ((username == "admin") and (passwd == "admin123") and (not (role == "support"))):
    print("Access Granted !!!")
else:
    print("Access Not Granted !!!")

if ((username == "admin") and (passwd == "admin123") and (role != "support")):
    print("Access Granted !!!")
else:
    print("Access Not Granted !!!")
