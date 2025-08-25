from abc import ABC, abstractmethod
from enum import Enum

class Vehicle_Type(Enum):
    CAR = "CAR",
    BIKE = "BIKE",
    TRUCK = "TRUCK"

class Vehicle(ABC):
    def __init__(self, vno, vtype):
        self.vno = vno
        self.vtype = vtype

class Car(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.CAR)

class Bike(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.BIKE)

class Truck(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.TRUCK)


def main(vehicle, vno):
    if vehicle == "CAR":
        return Car(vno)
    elif vehicle == "BIKE":
        return Bike(vno)
    else:
        return Truck(vno)

if __name__ == "__main__":
    main("BIKE")


# If there is a new type of vehicle uis added like VAN. then the main function which generate the object needs to be updated in order to support the new Vrhicle type.
# Hence we can add the Factory patten. This is like based on the value it will generate the object. The value will directly look into the Vehicle type.
# Its like based on the ingredient the burgers are generated. Burger is the base class and cheese burger, veggi burger etc are the different classes.

