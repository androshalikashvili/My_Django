import pytest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle:

    @classmethod
    def setup_class(cls):
        print("Setting up class\n")


    @classmethod
    def teardown_class(cls):
        print("Tearing down class")


    def setup_method(self, method):
        print(f"Setting up {method}")

        self.vehicle = Vehicle("Toyota", "Camry", 2022)
        self.e_vehicle = ElectricVehicle("Tesla", "Model S", 2023)


    def teardown_method(self, method):
        print(f"Tearing down {method}\n")


    def test_fuel_up(self):
        assert self.vehicle.fuel_up == "Gas tank is now full or can move."
        assert self.e_vehicle.fuel_up == "This vehicle has no fuel tank!"

    def test_drive(self):
        assert self.vehicle.drive == "The Camry is now driving."
        assert self.e_vehicle.drive == "The Model S is now driving."

    def test_charge(self):
        assert self.e_vehicle.charge == "The vehicle is now charged."
