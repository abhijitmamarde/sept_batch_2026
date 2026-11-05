# Person and Car are class objects
# a car has an owner
# a person may have multiple cars

# Assignment
# Book and Author relations
# author - written books count
# book - year, pages count

class Person:

    def __init__(self, name):
        self.name = name
        self.cars = []

    def buys_car(self, car):
        self.cars.append(car)

    def print(self):
        print("Name: ", self.name)
        print("Has Cars:")

        for car in self.cars:
            print(car.name)

class Car:

    def __init__(self, name):
        self.name = name

    def print_owner_name(self):
        print("Car is:", self.name)    
        print("Owner name is:", self.name) # TODO: get actual owner name here!   


car_nixxon = Car("Nixon")
car_bmw = Car("BMW")
car_ferrari = Car("Ferrari")



sagar = Person("Sagar")
manish = Person("Manish")
pranjali = Person("Pranjali")

sagar.buys_car(car_nixxon)
manish.buys_car(car_bmw)
pranjali.buys_car(car_ferrari)
pranjali.buys_car(car_nixxon)

sagar.print()
manish.print()
pranjali.print()

# sagar = Person("Sagar", [car_nixxon])
# manish = Person("Manish", [car_bmw])
# pranjali = Person("Pranjali", [car_ferrari])


car_nixxon.print_owner_name()