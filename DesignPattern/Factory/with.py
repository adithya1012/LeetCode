from abc import ABC, abstractmethod
from enum import Enum


class Vehicle_Type(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


class Vehicle(ABC):
    def __init__(self, vno, vtype):
        self.vno = vno
        self.vtype = vtype

    @abstractmethod
    def get_info(self):
        """Abstract method to get vehicle information"""
        pass

    def __str__(self):
        return f"{self.vtype.value} with vehicle number: {self.vno}"


class Car(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.CAR)

    def get_info(self):
        return f"This is a car with vehicle number {self.vno}"


class Bike(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.BIKE)  # Fixed: was Vehicle_Type.CAR

    def get_info(self):
        return f"This is a bike with vehicle number {self.vno}"


class Truck(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, Vehicle_Type.TRUCK)  # Fixed: was Vehicle_Type.CAR

    def get_info(self):
        return f"This is a truck with vehicle number {self.vno}"


# Factory Pattern Implementation
class VehicleFactory:
    """Factory class to create vehicle objects"""

    @staticmethod
    def create_vehicle(vehicle_type, vno):
        """
        Factory method to create vehicle instances

        Args:
            vehicle_type (str): Type of vehicle to create
            vno (str): Vehicle number

        Returns:
            Vehicle: Instance of the requested vehicle type

        Raises:
            ValueError: If vehicle_type is not supported
        """
        vehicle_type = vehicle_type.upper()

        if vehicle_type == "CAR":
            return Car(vno)
        elif vehicle_type == "BIKE":
            return Bike(vno)
        elif vehicle_type == "TRUCK":
            return Truck(vno)
        else:
            raise ValueError(f"Unsupported vehicle type: {vehicle_type}")

    @staticmethod
    def get_supported_types():
        """Returns list of supported vehicle types"""
        return [vtype.value for vtype in Vehicle_Type]


def main():
    """Demonstration of the Factory Pattern"""
    factory = VehicleFactory()

    # Create different types of vehicles using the factory
    try:
        car = factory.create_vehicle("CAR", "ABC123")
        bike = factory.create_vehicle("BIKE", "XYZ789")
        truck = factory.create_vehicle("TRUCK", "DEF456")

        # Display vehicle information
        vehicles = [car, bike, truck]

        print("Created vehicles using Factory Pattern:")
        print("-" * 40)
        for vehicle in vehicles:
            print(f"• {vehicle}")
            print(f"  Info: {vehicle.get_info()}")
            print()

        print(f"Supported vehicle types: {factory.get_supported_types()}")

        # Example of error handling
        print("\nTrying to create unsupported vehicle type:")
        try:
            invalid_vehicle = factory.create_vehicle("AIRPLANE", "FLY123")
        except ValueError as e:
            print(f"Error: {e}")

    except ValueError as e:
        print(f"Error creating vehicle: {e}")


if __name__ == "__main__":
    main()