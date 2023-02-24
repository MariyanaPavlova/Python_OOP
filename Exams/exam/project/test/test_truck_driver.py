from project.truck_driver import TruckDriver

from unittest import TestCase, main

class testTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck = TruckDriver("Yavor", 5.50)

    def test_init(self):
        self.assertEqual('Yavor', self.truck.name)
        self.assertEqual(5.50, self.truck.money_per_mile)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_earned_money(self):
        with self.assertRaises(ValueError)as ex:
            self.truck.earned_money = -1
        self.assertEqual("Yavor went bankrupt.", str(ex.exception))

    def test_earned_money_0(self):
        self.truck.earned_money = 5.15
        self.assertEqual('Yavor', self.truck.name)
        self.assertEqual(5.50, self.truck.money_per_mile)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(5.15, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_earned_money_1(self):
        self.truck.earned_money = 0
        self.assertEqual('Yavor', self.truck.name)
        self.assertEqual(5.50, self.truck.money_per_mile)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.earned_money)
        self.assertEqual(0, self.truck.miles)

    def test_add_cargo_offer(self):
        self.truck.available_cargos = {"Russe": 100}
        with self.assertRaises(Exception)as ex:
            self.truck.add_cargo_offer("Russe", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_1(self):
        self.truck.available_cargos = {"Russe": 100}
        result = self.truck.add_cargo_offer("Montana", 200)
        self.assertEqual({"Russe": 100, "Montana": 200}, self.truck.available_cargos)
        self.assertEqual(f"Cargo for 200 to Montana was added as an offer.", result)

    def test_drive_best_cargo_offer(self):
        self.truck.available_cargos = {}
        self.cargo_location = 0
        result = self.truck.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)
        self.assertEqual({}, self.truck.available_cargos)
        self.assertEqual(0, self.truck.miles)

    def test_drive_best_cargo_offer_1(self):
        self.truck.available_cargos = {"Russe": 100, "Montana": 200}
        result = self.truck.drive_best_cargo_offer()
        self.assertEqual(1100, self.truck.earned_money)
        self.assertEqual(200, self.truck.miles)
        self.assertEqual("Yavor is driving 200 to Montana.", result)


    def test_check_for_activities_250(self):
        self.truck.available_cargos = {"Montana": 250}
        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(250, self.truck.miles)
        self.assertEqual(1355.0, self.truck.earned_money)
        self.assertEqual(5.5, self.truck.money_per_mile)


    def test_check_for_activities_1000(self):
        self.truck.available_cargos = {"Montana": 1000}
        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(1000, self.truck.miles)
        self.assertEqual(5375.0, self.truck.earned_money)
        self.assertEqual(5.5, self.truck.money_per_mile)

    def test_check_for_activities_1500(self):
        self.truck.available_cargos = {"Montana": 1500}
        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(1500, self.truck.miles)
        self.assertEqual(7585.0, self.truck.earned_money)
        self.assertEqual(5.5, self.truck.money_per_mile)


    def test_check_for_activities_10000(self):
        self.truck.available_cargos = {"Montana": 10000}
        result = self.truck.drive_best_cargo_offer()

        self.assertEqual(10000, self.truck.miles)
        self.assertEqual(43250.0, self.truck.earned_money)
        self.assertEqual(5.5, self.truck.money_per_mile)


    def test_repr(self):
        self.truck.miles = 5
        result = self.truck.__repr__()
        self.assertEqual("Yavor has 5 miles behind his back.", result)


if __name__ == "__main__":
    main()