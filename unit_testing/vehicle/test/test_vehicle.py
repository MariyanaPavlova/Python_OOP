from unittest import TestCase, main

from vehicle.project.vehicle import Vehicle


class VehicleTest(TestCase):
    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_raises_error_fuel_not_enough(self):

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_drive_fuel_not_changed(self):
        distance = 50
        remaining_fuel = 37.5

        self.vehicle.drive(distance)
        self.assertEqual(remaining_fuel, self.vehicle.fuel)

    def test_drive_reduces_fuel(self): #self.fuel -= fuel_needed
        distance = 20
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance #25

        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed #75
        self.assertEqual(expected_result, self.vehicle.fuel)

        self.vehicle.drive(distance)
        expected_result = self.FUEL - fuel_needed - fuel_needed #50
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_refuel_raises_error_when_capacity_overflow(self):
        capacity = self.FUEL

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_fuel_up(self):
        capacity = self.FUEL
        self.vehicle.drive(20)
        self.vehicle.refuel(20)
        expected_result = 75 + 20
        self.assertEqual(expected_result, self.vehicle.fuel)

    def test_str(self):
        expected = f"The vehicle has {self.HORSE_POWER} " \
        f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"
        self.assertEqual(expected, self.vehicle.__str__())