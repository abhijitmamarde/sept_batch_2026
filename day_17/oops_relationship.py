# Contains
# Engine - Petrol 1600CC, Diesel 2000CC
# Car Models 
#   - Swift Petrol 1600CC 
#   - Swift Diesel 2000CC
# Car -> Has a Engine 

class Engine:
    pass

class P1600cc(Engine):
    pass

class D2000cc(Engine):
    pass

# Wrong approach with Inhertiance -> car does not have attributes of Engine; It has one engine
# class Car(Engine):
#     pass

class Car:

    def __init__(self, car_engine):
        self.engine = car_engine
        pass

e1 = P1600cc()
e2 = P1600cc()

c1 = Car(e1)
c2 = Car(e2)