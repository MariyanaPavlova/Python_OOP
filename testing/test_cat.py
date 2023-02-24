class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False

#INES
from unittest import TestCase, main

class CatTests(TestCase):
    def test_increase_size(self):
        cat = Cat("TestCat")
        self.assertEqual(0, cat.size)

        cat.eat()
        self.assertEqual(1, cat.size)

    def test_fed(self):
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)

        cat.eat()
        self.assertTrue(cat.fed)

    def test_cannot_eat_already_fed_raises(self):
        #Arrange
        cat = Cat("TestCat")
        cat.eat()

        #Act
        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cannot_fall_asleep_not_fed_raises(self):
        #Arrange
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_not_sleepy_after_sleeping(self):
        #Arrange
        cat = Cat("TestCat")
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        cat.eat()
        self.assertTrue(cat.sleepy)

        #Act
        cat.sleep()

        #Assert
        self.assertFalse(cat.sleepy)

if __name__ == '__main__':
    main()

#DONCHO
import unittest

class TestsCat(unittest.TestCase):
    NAME = "Pepelyashka"

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect__size_increased(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test__eat__expect__fed_True(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test__eat__when_fed_True_exp_to_raise(self):
        self.cat.eat()

        with self.assertRaises(Exception) as context:
            self.cat.eat()

        self.assertIsNotNone(context)
        self.assertEqual('Already fed.', str(context.exception))

    def test_sleep__when_fed_is_false__expect_to_raise(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test_sleep_expect_sleepy_to_be_false(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()