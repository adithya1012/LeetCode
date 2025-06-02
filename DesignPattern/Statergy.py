# WITHOUT STRATEGY PATTERN
# class vehicle:
#     def __init__(self):
#         self.vehicle = []
#
#     def drive(self):
#         print("This is a normal Drive")
#
#     def add_vehicle(self, vehicle):
#         self.vehicle.append(vehicle)
#
#
# class PassenderVehicle(vehicle):
#     def details(self):
#         print("Passanger: ",self.vehicle)
#
# class SportsVehicle(vehicle):
#     def drive(self): # this is a duplicate code
#         print("special drive capacity")
#
#     def details(self):
#         print("Sports: " , self.vehicle)
#
#
# class offroadVehicle(vehicle):
#     def drive(self): # this is a duplicate code
#         print("special drive capacity")
#     def details(self):
#         print("offroad: ", self.vehicle)
#
# o = offroadVehicle()
# o.add_vehicle("v1")
# o.add_vehicle("v2")
# o.add_vehicle("v3")
# o.details()
# o.drive()

# WITH STRATEGY PATTERN

from abc import ABC, abstractmethod


class DrivePattern:
    @abstractmethod
    def drive(self):
        pass

class NormalDrive(DrivePattern):
    def drive(self):
        print("Normal Drive")
class SpecialDrive(DrivePattern):
    def drive(self):
        print("Special Drive")

class vehicle:
    def __init__(self, drive_stratergy: DrivePattern):
        self.vehicle = []
        self.obj = drive_stratergy

    def drive(self):
        self.obj.drive()

    def add_vehicle(self, vehicle):
        self.vehicle.append(vehicle)


class PassenderVehicle(vehicle):
    def details(self):
        print("Passanger: ", self.vehicle)


class SportsVehicle(vehicle):
    def details(self):
        print("Sports: ", self.vehicle)


class offroadVehicle(vehicle):
    def details(self):
        print("offroad: ", self.vehicle)


o = offroadVehicle(SpecialDrive())
o.add_vehicle("v1")
o.add_vehicle("v2")
o.add_vehicle("v3")
o.details()
o.drive()

# So not drive method is not defined in any of the class except in the SpecialDrive and NormalDrive.
# This will avoid the duplicate code