from abc import ABC, abstractmethod
import enum


class Vehicle_Type(enum.Enum):
    CAR = 2
    BIKE = 1
    TRUCK = 3

class Vehicle:
    def __init__(self, type, number_plate):
        self.type = type
        self.number_plate = number_plate

    @abstractmethod
    def number_of_wheel(self):
        pass

    def contat(self):
        print("To book any vehicle call 26051519876")

class Car(Vehicle):
    def __init__(self, number_plate):
        super().__init__(Vehicle_Type.CAR, number_plate)

    def number_of_wheel(self):
        print("There are 4 wheels in this vehicle")



if __name__ == "__main__":
    obj = Car("ABCDCAR")
    obj.contat()
    obj.number_of_wheel()

