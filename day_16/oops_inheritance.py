# inheritance - one important pillar
# close to real world inheritance - property, biologically (get some physical traits from our parents)
# OOPS - parent / base class and derived / child class
# - derived class inherits the properties from base class

# Assignment: Book and Author OOPS model
class Person:
    name = ""
    age = 0
    country_citizen = ""
    gender = "M"

    def __init__(self, name, age, gender, country_citizen="Indian"):
        self.name = name
        self.age = age
        self.gender = gender
        self.country_citizen = country_citizen
        
    def change_name(self, new_name):
        self.name = new_name

    def change_citizenship(self, new_citizenship):
        self.country_citizen = new_citizenship

    def print(self):
        print(f"Person name: {self.name}, age: {self.age} years. Gender: {self.gender}; Citizen of: {self.country_citizen}")

# child Student -> derived from base class/parent class Person
# Now Student inherits EVERYTHING from Person class
class Student(Person):

    course_name = ""
    qualitfication = ""

    # Version 1, derived class passes the required params for parent's constructor
    # def __init__(self, course_name, qualitfication):
    #     super().__init__("noname", age=7, gender="NA")
    #     self.course_name = course_name
    #     self.qualitfication = qualitfication

    # Version 2, derived class constructor has all required params for parent class, and uses those to call parent's constructor
    def __init__(self, name, age, gender, country_citizen, course_name, qualitfication):
        super().__init__(name, age, gender, country_citizen)
        self.course_name = course_name
        self.qualitfication = qualitfication

    def assign_course(self, new_course_name):
        self.course_name = new_course_name

    def assign_qualitfication(self, new_qualitfication):
        self.qualitfication = new_qualitfication

    def print(self):
        # overwride the base class print method 
        # print(f"Student name: {self.name}, age: {self.age} years. Gender: {self.gender}")

        # 1st call the base class version
        super().print()

        # 2nd step call the additional things required for derived class
        print("Current Qualification:", self.qualitfication)
        print("Pursuing course:", self.course_name)


p = Person("Abhijeet", 42, "M")
p.change_name("Abhijit")
p.change_citizenship("Indian")
p.print()

s = Student("Manish", 30, "M", "Indian", "BE Comp", "12th")  # Version 2
# s = Student("BE Comp", "12th")  # Version 1
s.change_name("Sagar")
s.change_citizenship("Indian")
s.assign_course("Diploma")
s.assign_qualitfication("10th Standard")
s.print()
