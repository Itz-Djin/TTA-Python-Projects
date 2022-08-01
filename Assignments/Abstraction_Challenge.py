from abc import ABC, abstractmethod

#Created abstract parent class
class Vehicle(ABC):
    #defines the abstract class, preventing any objects to be made of this class
    @abstractmethod
    def go(self):
        pass

#created child class
class Car(Vehicle):

    def go(self):
        print("you drive the car")

#created child class
class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcycle")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go
car.go()
motorcycle.go()