# modules and packages
# these are used in bigger python projects
# to distribute your code in different modules/packages (python files)

# module 
# ============================================================================================
# any python file, can act as a module

# built in modules/packages - https://docs.python.org/3/py-modindex.html
# third party modules/packages - https://pypi.org/
import sys
# sys.argv - Commandline args
import types

# types.NoneType
# types.FunctionType


# 1st way, import specific module, and then use that module everytime while calling the func
import my_greet_module

my_greet_module.greet_user()
my_greet_module.greet_user("Abhijit")
my_greet_module.check_if_valid_username("abhijit")

# 2nd way, import specific funcs/attributes
# from my_greet_module import greet_user
# from my_greet_module import check_if_valid_username
from my_greet_module import greet_user, check_if_valid_username

greet_user()
greet_user("Sagar")
check_if_valid_username("Sagar")

# 3rd / 1st sub way
import my_greet_module as m
m.greet_user()
m.greet_user("Manish")
m.check_if_valid_username("Manish")

# 4th / 2nd sub way
from my_greet_module import greet_user as f1
from my_greet_module import check_if_valid_username as f2
f1()
f1("Pranjali")
f2("Pranjali")


# from my_calc_module import myadd, mysub, myabssub
from my_greet_module import myadd, mysub, myabssub

myadd(30, 45)
mysub(30, 45)
myabssub(30, 45)


# package 
# ============================================================================================
# any directory with 2 things:
# __init__.py -> file
# atleast one other .py file
import myutil.greet

myutil.greet.greet_user_v2()
myutil.greet.greet_user_v2("Abhijit")
myutil.greet.check_if_valid_username_v2("Abhijit")

from myutil.greet import greet_user_v2, check_if_valid_username_v2

greet_user_v2()
greet_user_v2("Abhijit")
check_if_valid_username_v2("Abhijit")

from myutil.math import myadd_v2, mysub_v2, myabssub_v2
myadd_v2(30, 45)
mysub_v2(30, 45)
myabssub_v2(30, 45)

# What is the diff between a module and package
# Its all about structure/organization/categorization of code
# module is just one file
# package is collection of files (can be one file too)

# Assignment
# ------------------
# Menu, add user, is valid for voting, list all users ...
# categorize it in diff modules; pacakges 
# - user_interaction, menu, input etc
# - utils funcs - is age valid for voting, is citzenship valid for voting