class Car:
    @staticmethod
    def start():
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped..")

class ToyotaCar(Car):
    def __init__(self, brand):
        # self.name = name
        self.brand = brand

class Fortuner(ToyotaCar): #single inheritance
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel")
car1.start() #multi level inheritance

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())