class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return (f'{self.name} has saved {self.money} money.')

#DONCHO
import unittest

class WorkerTest(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

               #ACT    ARANGE      ASSERT
    def test__init__valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)


    def test__rest__expect_energy_to_be_increased(self):
        self.worker.rest()
        self.worker.rest()
        self.assertEqual(self.ENERGY + 2, self.worker.energy)


    def test__work__when_energy_is_0__exp_to_raise(self):
        worker = Worker(self.NAME, self.SALARY, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))


    def test__work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
        self.worker.work()
        self.worker.work()

        self.assertEqual(2*self.SALARY, self.worker.money)


    def test__work__when_enough_energy__expect_energy_to_decrement(self):
        self.worker.work()

        self.assertEqual(self.ENERGY-1, self.worker.energy)


    def test_get_info__expect_correct_result(self):
        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved {0} money.'

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()


 #INES
from unittest import TestCase, main

class WorkerTest(TestCase):
    def test_worker_is_initialized_with_correctly(self):
        # Arrange
        worker = Worker("Test", 100, 10)
        # Act
        # Assert
        self.assertEqual('Test', worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        #Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)
        #Act
        worker.rest()

        #Assert
        self.assertEqual(11, worker.energy)

    def test_worker_can_not_work_with_0_energy_raises(self):
        #Arrange
        worker = Worker('Test', 100, 0)

        #Act + Assert
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_with_neg_energy_raises(self):
        worker = Worker('Test', 100, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_is_payed_after_working(self):
        #Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(0, worker.money)

        #Act
        worker.work()
        #Assert
        self.assertEqual(100, worker.money)

        #Act
        worker.work()
        # Assert
        self.assertEqual(200, worker.money)

    def test_energy_is_decreased_after_working(self):
        #Arrange
        worker = Worker('Test', 100, 10)
        self.assertEqual(10, worker.energy)

        #Act
        worker.work()
        #Assert
        self.assertEqual(9, worker.energy)

    def test_get_info(self):
        #Arrange
        worker = Worker('Test', 100, 10)

        result = worker.get_info()
        expected = 'Test has saved 0 money.'

        self.assertEqual(expected, result)
        #допълнително
        worker.work()
        result = worker.get_info()
        expected = 'Test has saved 100 money.'

        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()