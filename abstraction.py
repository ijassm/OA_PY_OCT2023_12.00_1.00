# Import required modules
from abc import ABC, abstractmethod


# Create Abstract base class
class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Create abstract method
    @abstractmethod
    def printDetails(self):
        pass

    # Create concrete method
    def accelerate(self):
        print("speed up ...")

    def break_applied(self):
        print("Car stop")


# Create a child class
class Hatchback(Car):
    # def printDetails(self):
    #     print("Brand:", self.brand)
    #     print("Model:", self.model)
    #     print("Year:", self.year)

    def Sunroof(self):
        print("Not having this feature")


# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def Sunroof(self):
        print("Available")


car1 = Hatchback("Maruti", "Alto", "2022")

car1.printDetails()
car1.accelerate()
