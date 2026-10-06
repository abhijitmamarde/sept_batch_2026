# input function, command line (parameters)

name = input("Enter your name:")
# name = "abhijit"
print(f"Welcome {name}")

age = input("Enter your age:")
# conversion from string to float, and then float to int
age = int(float(age))

print(f"Your age is: {age}")
print(f"age type is: {type(age)}")

is_indian = input("Are you indian? yes/no:")
if (is_indian.lower() == "yes"):
    is_indian = True
else:
    is_indian = False

if (is_indian is True) and (age >= 18):
    print(f"You are allowed to vote.")
else:
    print(f"You are not allowed to vote.")

