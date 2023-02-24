from unittest import TestCase, main

from project_train.train.train import Train


class TrainTest(TestCase):
    def setUp(self) -> None:
        self.train = Train('tutu', 3)


    def test_init(self):
        name = "tutu"
        capacity = 3
        train = Train(name, capacity)

        self.assertEqual(name, train.name)
        self.assertEqual(capacity, train.capacity)
        self.assertEqual([], train.passengers)


    def test_add_0(self):
        passenger1 = 'Gosho'
        result = self.train.add(passenger1)

        self.assertTrue(passenger1 in self.train.passengers)
        self.assertEqual('Added passenger Gosho', result)
        self.assertEqual(1, len(self.train.passengers))

    def test_add_1(self):
        passenger1 = 'Gosho'
        result = self.train.add(passenger1)

        with self.assertRaises(ValueError) as ex:
            self.train.add("Gosho")
        self.assertEqual("Passenger Gosho Exists", str(ex.exception))

    def test_add_2(self):
        passenger1 = 'Gosho'
        passenger2 = 'Ivan'
        passenger3 = 'Petar'

        self.train.passengers.append(passenger1)
        self.train.passengers.append(passenger2)
        self.train.passengers.append(passenger3)

        with self.assertRaises(ValueError) as ex:
            self.train.add("Gogo")
        self.assertEqual("Train is full", str(ex.exception))


    def test_remove_0(self):
        self.train.passengers = ['Gosho', 'Ivan', 'Petar']

        with self.assertRaises(ValueError) as ex:
            self.train.remove('Petko')
        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_1(self):
        self.train.passengers = ['Gosho', 'Ivan', 'Petar']

        result = self.train.remove('Gosho')
        self.assertEqual('Removed Gosho', result)
        self.assertTrue("Gosho" not in self.train.passengers)
        self.assertEqual(2, len(self.train.passengers))

if __name__ == '__main__':
    main()