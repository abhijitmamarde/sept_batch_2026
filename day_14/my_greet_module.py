from my_calc_module import myadd, mysub, myabssub
# from my_calc_module import myadd as _myadd
# from my_calc_module import mysub as _mysub
# from my_calc_module import myabssub as _myabssub

def greet_user(username="Guest"):
    print(f"Good day {username}, Welcome to the application!")

def check_if_valid_username(username):
    res = username.lower() in [
        "abhijit",
        "sagar",
        "manish",
        "pranjali",
    ]
    print(f"Checking if {username} is valid user, result is: {res}")

# def myadd(n1, n2):
#     return _myadd(n1, n2)

# def mysub(n1, n2):
#     return _mysub(n1, n2)

# def myabssub(n1, n2):
#     return _myabssub(n1, n2)

if __name__ == "__main__":

    # Ensures this part of code is NOT executed when included as m module
    # it executes only if this file is called from python on command line!
    import sys

    greet_user(sys.argv[1])
    check_if_valid_username(sys.argv[1])
    print("DONE CALLING my_gree_module program!!!")