import sys

class InvalidIsIndianTypeError(Exception):
    pass

try:
    name = sys.argv[1]
    age = sys.argv[2]
    age = int(float(age))
    is_indian = sys.argv[3]
    if is_indian.lower() not in ("yes", "no"):
        # raise Exception("...")
        # raise TypeError("Invalid input for is_indian! Only yes or no is allowed.")
        raise InvalidIsIndianTypeError("Invalid input for is_indian! Only yes or no is allowed.")
except InvalidIsIndianTypeError as err:
    print(err)
    sys.exit(-1)
except:
    print(f"Valid name, age and is indian or not (yes or no) arguments are required for program to continue!")
    sys.exit(-1)

print(f"Welcome {name}")
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

