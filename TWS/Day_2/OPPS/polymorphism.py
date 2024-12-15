class Car:

    def __init__(self,name):
        self.wheeles = 4
        self.name = name

    def brake(self):
        print(self.name, "has stopped for big car")

    def acc(self):
        print(self.name, "is accelerating")

class Minicar(Car):
    def __init__(self, name):
        super().__init__(name)
        pass

    def brake(self):
        print(self.name, "has stopped for Mini Car")

def use_brake(Car):   #DynamicMethodDispatch
    Car.brake()

big_car = Car("AUDI")

mini_car = Minicar("ALTO")

use_brake(mini_car)
use_brake(big_car)