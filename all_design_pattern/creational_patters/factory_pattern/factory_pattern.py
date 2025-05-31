"""
What is factory pattern?
The factory pattern is a creational design pattern used in object oriented programming.it provides a way to create a objects without specifying the exact class of the object what will be created.insted the instantaion is delegated to a method called a "factory method"

What is the use of factory pattern?
->
    1.Encapsulates object creation logic
    -> you can centralize and isolate the logic of creating objects,making you code cleaner and easier to manage.

    2.Support open/closed principle.
    -> you can add new types of objects without changing the client code.this makes your system more extensible

    3.Promotes loose coupling.
    -> The client code dosent need to know the specific class name.it relies only on interfaces or abstract classes

"""
from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start():
        raise NotImplementedError

class Bike(Vehicle):

    def start(self):
        print('Start method of bike')

    def break_funct(self):
        print('breaked')

class Car(Vehicle):
    def start(self):
        print(f"Start method of Car")
    def break_funct(self):
        print(f"Break function of Car")


class VehicleFactory:

    @staticmethod
    def get_vehicle(vehicle_type):
        if vehicle_type == 'car':
            return Car()
        elif vehicle_type == 'bike':
            return Bike()
        else:
            raise ValueError("Invalid vehicle Type")

if __name__ == "__main__":
    # bike_object = Bike()
    # bike_object.start()
    # bike_object.break_funct()    
    car = VehicleFactory.get_vehicle('car')

    car.start()
    car.break_funct()