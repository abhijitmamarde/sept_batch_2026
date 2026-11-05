# OOPS - Object Oriented Programming System
# Procedural Approach - Common / seen so far

# Everything as an Object
# Person, Student, Car - Objects of a real world

# An object can have attributes, methods
# attributes -> physical characteristics real world, data in programming world
# methods -> is to operate the object in real world; functions which operate on the instace of the class/object
# - are the functions, which operates on the instance of the class (self)

# Person -> has a Car -> class Person, class Car, relationship bet a car and a person.


# how to define class; bare minimum
# class Person:
#     pass

class Person:
    # name = ""
    # age = 0
    is_indian_citizen = False

    def __init__(self, name, age=0):
        """Actual constructor function"""
        self.name = name
        self.age = age

    def can_vote(self):
        if (self.age >= 18) and (self.is_indian_citizen is True):
            return True
        return False

    def change_citizenship(self, country):
        if country.lower() == "india":
            self.is_indian_citizen = True
            return

        self.is_indian_citizen = False
        


# how to create instance
p = Person("Sagar")
print(type(p))
print(isinstance(p, Person))

print(p)
print(p.name, p.age)
print("p can vote?", p.can_vote())

# Calling the constructor
p2 = Person("Abhijit", 42)
p2.change_citizenship("india")
print(p2)
print(p2.name, p2.age, p2.is_indian_citizen)

print("p2 can vote?", p2.can_vote())
