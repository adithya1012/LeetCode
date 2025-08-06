import enum
from abc import ABC, abstractmethod
from typing import Optional


class VehicleType(enum.Enum):
    CAR = 1
    BIKE = 2
    TRUCK = 3


# Vehicle hierarchy
class Vehicle(ABC):
    def __init__(self, vehicle_no: str):
        self.vehicle_no = vehicle_no

    @abstractmethod
    def get_vehicle_type(self) -> VehicleType:
        pass


class Car(Vehicle):
    def get_vehicle_type(self):
        return VehicleType.CAR


class Bike(Vehicle):
    def get_vehicle_type(self):
        return VehicleType.BIKE


class Truck(Vehicle):
    def get_vehicle_type(self):
        return VehicleType.TRUCK


# Spot Class
class Spot:
    def __init__(self, spot_no: int, allowed_type: VehicleType):
        self.spot_no = spot_no
        self.allowed_type = allowed_type
        self.vehicle: Optional[Vehicle] = None

    def is_available(self):
        return self.vehicle is None

    def can_fit(self, vehicle: Vehicle):
        return self.allowed_type == vehicle.get_vehicle_type()

    def park(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def unpark(self):
        self.vehicle = None


# Level Class
class Level:
    def __init__(self, floor_no: int, spot_config: dict[VehicleType, int]):
        self.floor_no = floor_no
        self.spots: list[Spot] = []
        self._init_spots(spot_config)

    def _init_spots(self, spot_config: dict[VehicleType, int]):
        spot_no = 1
        for v_type, count in spot_config.items():
            for _ in range(count):
                self.spots.append(Spot(spot_no, v_type))
                spot_no += 1

    def get_available_spots(self):
        return [spot for spot in self.spots if spot.is_available()]

    def __str__(self):
        return f"Level {self.floor_no}"


# Strategy Interface
class ParkingStrategy(ABC):
    @abstractmethod
    def find_spot(self, levels: list[Level], vehicle: Vehicle) -> Optional[tuple[Level, Spot]]:
        pass


# First Fit Parking Strategy
class FirstFitStrategy(ParkingStrategy):
    def find_spot(self, levels: list[Level], vehicle: Vehicle) -> Optional[tuple[Level, Spot]]:
        for level in levels:
            for spot in level.get_available_spots():
                if spot.can_fit(vehicle):
                    return (level, spot)
        return None


# Singleton Parking Lot
class ParkingLot:
    _instance = None

    def __init__(self, strategy: ParkingStrategy):
        if ParkingLot._instance is not None:
            raise Exception("Singleton violation!")
        self.levels: list[Level] = []
        self.strategy = strategy
        ParkingLot._instance = self

    @staticmethod
    def get_instance(strategy: ParkingStrategy):
        if ParkingLot._instance is None:
            ParkingLot(strategy)
        return ParkingLot._instance

    def add_level(self, level: Level):
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle) -> str:
        res = self.strategy.find_spot(self.levels, vehicle)
        if res:
            level, spot = res
            spot.park(vehicle)
            return f"Parked at Level {level.floor_no}, Spot {spot.spot_no}"
        return "No suitable spot available"

    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            for spot in level.spots:
                if spot.vehicle == vehicle:
                    spot.unpark()
                    return f"Unparked from Level {level.floor_no}, Spot {spot.spot_no}"
        return "Vehicle not found"


# Demo
class Demo:
    @staticmethod
    def run():
        strategy = FirstFitStrategy()
        pl = ParkingLot.get_instance(strategy)

        # Level 1: 2 Car, 2 Bike, 1 Truck
        level1 = Level(1, {
            VehicleType.CAR: 2,
            VehicleType.BIKE: 2,
            VehicleType.TRUCK: 1
        })

        # Level 2: 1 Car, 1 Truck
        level2 = Level(2, {
            VehicleType.CAR: 1,
            VehicleType.TRUCK: 1
        })

        pl.add_level(level1)
        pl.add_level(level2)

        car = Car("KA-01-CAR")
        bike = Bike("KA-01-BIKE")
        truck = Truck("KA-01-TRUCK")

        print(pl.park_vehicle(car))     # e.g., Level 1, Spot 1
        print(pl.park_vehicle(bike))    # Level 1, Spot 3
        print(pl.park_vehicle(truck))   # Level 1, Spot 5

        print(pl.unpark_vehicle(car))   # Unparked
        print(pl.park_vehicle(car))     # Re-parks to available spot


if __name__ == "__main__":
    Demo.run()
