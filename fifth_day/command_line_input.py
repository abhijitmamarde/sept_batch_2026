import sys

# name = input("Enter your name:")
# age = input("Enter your age:")
# is_indian = input("Are you indian? yes/no:")

print(f"Type of argv: {type(sys.argv)}")
print(f"args passed are: {sys.argv}")
name = sys.argv[1]
# name = "abhijit"
age = sys.argv[2]
is_indian = sys.argv[3]

print(f"Welcome {name}")


# conversion from string to float, and then float to int
age = int(float(age))

print(f"Your age is: {age}")
print(f"age type is: {type(age)}")


if (is_indian.lower() == "yes"):
    is_indian = True
else:
    is_indian = False

if (is_indian is True) and (age >= 18):
    print(f"You are allowed to vote.")
else:
    print(f"You are not allowed to vote.")

