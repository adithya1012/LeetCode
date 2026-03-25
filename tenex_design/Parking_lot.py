import datetime
from enum import Enum


class VehicleTypes(Enum):
    BIKE = 1
    CAR = 2
    TRUCK = 3

class Vehicle:
    def __init__(self, type, lisence_no):
        self.type = type
        self.lisence_no = lisence_no

    def get_vehicle_type(self):
        return self.type

class Car(Vehicle):
    def __init__(self, lisence_no):
        super().__init__(VehicleTypes.CAR,lisence_no)

class Bike(Vehicle):
    def __init__(self, lisence_no):
        super().__init__(VehicleTypes.BIKE,lisence_no)

class Truck(Vehicle):
    def __init__(self, lisence_no):
        super().__init__(VehicleTypes.TRUCK,lisence_no)

class ParkingSpotType:
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    ACCESSIBLE = 4

class ParkingSpot:
    def __init__(self, type, id):
        self.is_available = True
        self.vehicle = None
        self.parking_type = type
        self.id = id

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.is_available = False

    def unpark_vehicle(self):
        self.vehicle = None
        self.is_available = True

    def is_available(self):
        return self.is_available

class SmallParkingSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(ParkingSpotType.SMALL, id)

class MediumParkingSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(ParkingSpotType.MEDIUM, id)

class LargeParkingSpot(ParkingSpot):
    def __init__(self, id):
        super().__init__(ParkingSpotType.LARGE, id)

class ParkingTicket:
    def __init__(self, id, vehicle:Vehicle, spot: ParkingSpot):
        self.id = id
        self.vehicle = vehicle
        self.time = datetime.datetime.now()
        self.parking_spot = spot

    def generate_ticklet(self):
        return self.id

class ParkingLot:
    instance = None
    def __init__(self, address):
        self.address = address
        self.small_parking_spots = []
        self.medium_parking_spots = []
        self.large_parking_spots = []
        self.parking_spot_mapping = {
            ParkingSpotType.SMALL: self.small_parking_spots,
            ParkingSpotType.MEDIUM: self.medium_parking_spots,
            ParkingSpotType.LARGE: self.large_parking_spots,
        }

    @staticmethod
    def get_instance():
        if not ParkingLot.instance:
            ParkingLot.instance = ParkingLot("ADRESS")
        return ParkingLot.instance

    def add_small_ParkingSpot(self, count):
        for i in range(count):
            self.small_parking_spots.append(SmallParkingSpot(f"{i}-small"))

    def add_medium_ParkingSpot(self, count):
        for i in range(count):
            self.medium_parking_spots.append(MediumParkingSpot(f"{i}-medium"))

    def add_large_ParkingSpot(self, count):
        for i in range(count):
            self.large_parking_spots.append(LargeParkingSpot(f"{i}-large"))

    def park_vehicle(self, vehicle, parking_spot_type):
        parking_spots = self.parking_spot_mapping.get(parking_spot_type, [])
        for ps in parking_spots:
            if ps.is_available:
                ps.park_vehicle(vehicle)
                return ps
        return None

    def unpark_vehicle(self, ticket:ParkingTicket):
        ticket.parking_spot.is_available = False
        return True

def demo():
    parking_lot = ParkingLot.get_instance()
    parking_lot.add_medium_ParkingSpot(100)
    parking_lot.add_small_ParkingSpot(100)
    parking_lot.add_large_ParkingSpot(100)

    car = Car("123-XYZ")
    ps = parking_lot.park_vehicle(car, ParkingSpotType.MEDIUM)

    ticket = ParkingTicket(f"{car.lisence_no} +{datetime.datetime.now()}", car, ps)
    ticket.generate_ticklet()


    parking_lot.unpark_vehicle(ticket)

demo()














