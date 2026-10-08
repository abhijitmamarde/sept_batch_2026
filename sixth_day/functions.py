# Functions
# block of common-code which we have to trigger multiple times
# on specific conditions

# func definition
def greet():
    print("Hello User, How are you today!")

    for i in range(1, 4):
        print(f"{i}. Hope you are doing great!")


# trigger / calling the function
greet()


for i in range(1, 6):
    greet()
    print("XXxXxxx")

def greet_v2(name, age=0, is_indian=False):
    print(f"Hello {name}, and age is: {age}, is_indian: {is_indian}!")

    if (age>=18) and is_indian:
        return True
    else:
        return False

can_vote = greet_v2("abhi", 42, True)
print(f"can vote: {can_vote}")

can_vote = greet_v2("abhi", 10, True)
print(f"can vote: {can_vote}")

can_vote = greet_v2("sagar", 30, True)
print(f"can vote: {can_vote}")

can_vote = greet_v2("manish", 25, False)
print(f"can vote: {can_vote}")

# using defaults
can_vote = greet_v2("YYY")
print(f"can vote: {can_vote}")

# default way: Positional arg calling
# Keyword arg calling/passing
can_vote = greet_v2("aaa", is_indian=True, age=78)
can_vote = greet_v2(is_indian=True, age=78, name="aaa")
print(f"can vote: {can_vote}")

# write simple calculator with add, sub, div, mult functions
# and call it on user specifed command line arg

