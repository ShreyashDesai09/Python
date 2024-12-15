class Car:
    def __init__(self,name):
        self.wheels = 4    
        self.name = name

    def brake(self):
        print(self.name, " Has Stopped")

    def acceleration(self):
        print(self.name, " is accelerating")

class MiniCar(Car):

    def __init__(self,name):
        super().__init__(name)
        pass

    def brake(self):
        super().brake()
        pass

mini = MiniCar("WAGON R")
carr = Car("ALTO")
carr.brake()
carr.acceleration()
mini.brake()
carr.brake()