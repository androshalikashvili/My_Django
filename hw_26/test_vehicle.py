import unittest
from vehicle import Vehicle, ElectricVehicle

class TestVehicle(unittest.TestCase):

    def setUp(self):
        self.vehicle = Vehicle("Toyota", "Camry", 2022)
        self.e_vehicle = ElectricVehicle("Tesla", "Model S", 2023)

    def test_fuel_up(self):
        self.assertEqual(self.vehicle.fuel_up, "Gas tank is now full or can move.")
        self.assertEqual(self.e_vehicle.fuel_up, "This vehicle has no fuel tank!")

    def test_drive(self):
        self.assertEqual(self.vehicle.drive, "The Camry is now driving.")
        self.assertEqual(self.e_vehicle.drive, "The Model S is now driving.")

    def test_charge(self):
        self.assertEqual(self.e_vehicle.charge, "The vehicle is now charged.")

if __name__ == '__main__':
    unittest.main()
