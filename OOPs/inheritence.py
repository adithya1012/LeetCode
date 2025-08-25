class Vehicle:
    def __init__(self, name, model):
        self.name = name
        self.model = model


class GasVehicle(Vehicle):
    def __init__(self, name, model, type="Petrol"):
        super().__init__(name, model)
        self.type = type

class ElectricVehicle(Vehicle):
    def __init__(self, name, model, type):
        super().__init__(name, model)
        self.type = type

class HybridVehicle(GasVehicle, ElectricVehicle):
    def __init__(self, name, model, type="Petrol"):
        GasVehicle.__init__(name, model, "Petrol")
        ElectricVehicle.__init__(name, model, "Electric")

