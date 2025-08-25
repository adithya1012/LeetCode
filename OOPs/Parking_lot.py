from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum

# Constants
HOURLY_RATE = {
    'Car': 10,
    'Truck': 20,
    'Bike': 5
}


class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    BIKE = "Bike"


class Vehicle:
    def __init__(self, vno, vehicle_type):
        self.vehicle_no = vno
        self.vehicle_type = vehicle_type
        # ... other metadata of vehicle


class Car(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, VehicleType.CAR)


class Truck(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, VehicleType.TRUCK)


class Bike(Vehicle):
    def __init__(self, vno):
        super().__init__(vno, VehicleType.BIKE)


class Payment_method(ABC):
    def __init__(self, card_no):
        self.card_no = card_no

    @abstractmethod
    def payment(self, amount, cvv):
        pass


class Credit_card_payment(Payment_method):
    def __init__(self, card_no):
        super().__init__(card_no)

    def payment(self, amount, cvv):
        print(f"Processing credit card payment of ${amount}")
        print(f"Verifying CVV: {cvv}")
        # Simulate payment processing
        print("Credit card payment completed successfully")
        return True


class Debit_card_payment(Payment_method):
    def __init__(self, card_no):
        super().__init__(card_no)

    def payment(self, amount, cvv):
        print(f"Processing debit card payment of ${amount}")
        print(f"Verifying CVV: {cvv}")
        # Simulate payment processing
        print("Debit card payment completed successfully")
        return True


class Parking_spot(ABC):
    def __init__(self, id, spot_type):
        self.id = id
        self.spot_type = spot_type
        self.vehicle = None
        self.is_occupied = False

    @abstractmethod
    def can_park_vehicle(self, vehicle):
        pass

    def park_vehicle(self, vehicle):
        if self.can_park_vehicle(vehicle) and not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def unpark_vehicle(self):
        if self.is_occupied:
            self.vehicle = None
            self.is_occupied = False
            return True
        return False


class Car_parking_spot(Parking_spot):
    def __init__(self, id):
        super().__init__(id, VehicleType.CAR)

    def can_park_vehicle(self, vehicle):
        return isinstance(vehicle, Car)


class Truck_parking_spot(Parking_spot):
    def __init__(self, id):
        super().__init__(id, VehicleType.TRUCK)

    def can_park_vehicle(self, vehicle):
        return isinstance(vehicle, Truck)


class Bike_parking_spot(Parking_spot):
    def __init__(self, id):
        super().__init__(id, VehicleType.BIKE)

    def can_park_vehicle(self, vehicle):
        return isinstance(vehicle, Bike)


class Ticket:
    def __init__(self, id, vehicle, parking_spot, entry_time=None):
        self.id = id
        self.vehicle = vehicle
        self.parking_spot = parking_spot
        self.entry_time = entry_time or datetime.now()
        self.exit_time = None

    def update_exit_time(self, exit_time=None):
        self.exit_time = exit_time or datetime.now()

    def calculate_rate(self):
        if not self.exit_time:
            return 0

        duration_hours = (self.exit_time - self.entry_time).total_seconds() / 3600
        # Round up to the nearest hour
        duration_hours = max(1, int(duration_hours) + (1 if duration_hours % 1 > 0 else 0))

        vehicle_type_str = self.vehicle.vehicle_type.value
        rate = HOURLY_RATE.get(vehicle_type_str, 10)
        return duration_hours * rate


class EntryExit:
    def __init__(self, id):
        self.id = id

    def generate_ticket(self, vehicle, parking_spot):
        ticket_id = f"T_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{vehicle.vehicle_no}"
        return Ticket(ticket_id, vehicle, parking_spot)

    def process_exit(self, ticket):
        ticket.update_exit_time()
        return ticket.calculate_rate()


class Parking_lot:
    _instance = None

    def __init__(self, entry_exits=None, parking_spots=None):
        if Parking_lot._instance is not None:
            raise Exception("This class is a singleton!")

        self.entry_exits = entry_exits or []
        self.parking_spots = parking_spots or []
        self.active_tickets = {}  # ticket_id -> ticket mapping
        Parking_lot._instance = self

    @staticmethod
    def get_instance():
        if Parking_lot._instance is None:
            Parking_lot._instance = Parking_lot()
        return Parking_lot._instance

    def add_parking_spot(self, parking_spot):
        self.parking_spots.append(parking_spot)

    def add_entry_exit(self, entry_exit):
        self.entry_exits.append(entry_exit)

    def find_available_spot(self, vehicle):
        for spot in self.parking_spots:
            if not spot.is_occupied and spot.can_park_vehicle(vehicle):
                return spot
        return None

    def park_vehicle(self, vehicle, entry_exit_id=0):
        # Find available parking spot
        available_spot = self.find_available_spot(vehicle)
        if not available_spot:
            print(f"No available parking spot for vehicle {vehicle.vehicle_no}")
            return None

        # Park the vehicle
        if available_spot.park_vehicle(vehicle):
            # Generate ticket
            entry_exit = self.entry_exits[entry_exit_id] if entry_exit_id < len(self.entry_exits) else self.entry_exits[
                0]
            ticket = entry_exit.generate_ticket(vehicle, available_spot)
            self.active_tickets[ticket.id] = ticket

            print(f"Vehicle {vehicle.vehicle_no} parked at spot {available_spot.id}")
            print(f"Ticket generated: {ticket.id}")
            return ticket

        return None

    def unpark_vehicle(self, ticket_id, payment_method, cvv):
        if ticket_id not in self.active_tickets:
            print("Invalid ticket ID")
            return False

        ticket = self.active_tickets[ticket_id]

        # Calculate parking fee
        entry_exit = self.entry_exits[0]  # Use first entry/exit for processing
        amount = entry_exit.process_exit(ticket)

        print(f"Parking duration: {ticket.exit_time - ticket.entry_time}")
        print(f"Total amount: ${amount}")

        # Process payment
        if payment_method.payment(amount, cvv):
            # Unpark vehicle
            if ticket.parking_spot.unpark_vehicle():
                del self.active_tickets[ticket_id]
                print(f"Vehicle {ticket.vehicle.vehicle_no} successfully unparked from spot {ticket.parking_spot.id}")
                return True

        return False

    def get_parking_status(self):
        total_spots = len(self.parking_spots)
        occupied_spots = sum(1 for spot in self.parking_spots if spot.is_occupied)
        available_spots = total_spots - occupied_spots

        print(f"Parking Lot Status:")
        print(f"Total spots: {total_spots}")
        print(f"Occupied spots: {occupied_spots}")
        print(f"Available spots: {available_spots}")

        return {
            'total': total_spots,
            'occupied': occupied_spots,
            'available': available_spots
        }


class Demo:
    @staticmethod
    def run():
        # Initialize parking lot (Singleton)
        parking_lot = Parking_lot.get_instance()

        # Add entry/exit points
        entry_exit1 = EntryExit("E1")
        parking_lot.add_entry_exit(entry_exit1)

        # Add parking spots
        for i in range(1, 6):  # 5 car spots
            parking_lot.add_parking_spot(Car_parking_spot(f"C{i}"))

        for i in range(1, 4):  # 3 truck spots
            parking_lot.add_parking_spot(Truck_parking_spot(f"T{i}"))

        for i in range(1, 11):  # 10 bike spots
            parking_lot.add_parking_spot(Bike_parking_spot(f"B{i}"))

        print("=== Parking Lot System Demo ===\n")

        # Show initial status
        parking_lot.get_parking_status()
        print()

        # Create vehicles
        car1 = Car("CAR001")
        truck1 = Truck("TRUCK001")
        bike1 = Bike("BIKE001")

        # Park vehicles
        print("=== Parking Vehicles ===")
        ticket1 = parking_lot.park_vehicle(car1)
        ticket2 = parking_lot.park_vehicle(truck1)
        ticket3 = parking_lot.park_vehicle(bike1)
        print()

        # Show updated status
        parking_lot.get_parking_status()
        print()

        # Simulate some time passing and then unpark
        print("=== Unparking Vehicles ===")

        # Create payment methods
        credit_card = Credit_card_payment("1234-5678-9012-3456")
        debit_card = Debit_card_payment("9876-5432-1098-7654")

        # Unpark vehicles
        if ticket1:
            print("Unparking car...")
            parking_lot.unpark_vehicle(ticket1.id, credit_card, "123")
            print()

        if ticket2:
            print("Unparking truck...")
            parking_lot.unpark_vehicle(ticket2.id, debit_card, "456")
            print()

        # Show final status
        parking_lot.get_parking_status()


if __name__ == "__main__":
    Demo.run()