from abc import ABC, abstractmethod

#Created abstract parent class
class Vehicle(ABC):
    #defines the abstract class, preventing any objects to be instantiated of this class
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#created child class
class Car(Vehicle):

    def go(self):
        print("you drive the car")

    def stop(self):
        print("This car is stopped")

#created child class
class Motorcycle(Vehicle):

    def go(self):
        print("you ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()