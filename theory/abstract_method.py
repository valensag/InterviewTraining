#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has a declaration but does not have an implementation

#This is useful because prevents the user to create an object of a determinated class
# and make the user overide abstract methods in child class

from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO)

class Vehicle(ABC):
    
    @abstractmethod
    def go(self):
        pass

class Car(Vehicle):
    
    def go(self):
        logging.info(f"Let's go car")

class Motorcycle(Vehicle):

    def go(self):
        logging.info(f"Let's go motorcycle")

if __name__ == '__main__':

    yamaha = Motorcycle()
    yamaha.go()

    mazda = Car()
    mazda.go()
