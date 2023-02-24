from project_plantation.plantation import Plantation

from unittest import TestCase, main

class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(3)

    def test_init_(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation = Plantation(-5)
        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_1(self):
        self.plantation.workers = ['Jon', 'Gogo']
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('Gogo')
        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_2(self):
        self.plantation.workers = ['Jon', 'Gogo']
        result = self.plantation.hire_worker('Koko')
        self.assertEqual("Koko successfully hired.", result)
        self.assertEqual(['Jon', 'Gogo', 'Koko'], self.plantation.workers)

    def test_len_0(self):
        self.plantation.plants = {'Jon': []}
        self.assertEqual(0, self.plantation.__len__())

    def test_len_1(self):
        self.plantation.plants = {'Jon': ['popcorn']}
        self.assertEqual(1, self.plantation.__len__())

    def test_len_2(self):
        self.plantation.plants = {'Jon': ['popcorn'], "Goog": ['item', 'popcorn']}
        self.assertEqual(3, self.plantation.__len__())


    def test_planting(self):
        self.plantation.workers = ['Jon', 'Gogo']
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Koko', 'rize')
        self.assertEqual("Worker with name Koko is not hired!", str(ex.exception))
        self.assertTrue("Koko" not in self.plantation.workers)

    def test_planting_len_equal_limit(self):
        self.plantation.workers = ['Jon', 'Goog']
        self.plantation.plants = {'Jon': ['popcorn', 'greens'],
                                  'Goog': ['tomato']}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Jon', 'rise')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_len_2(self):
        self.plantation.workers = ['Jon', 'Goog']
        self.plantation.plants = {'Jon': ['popcorn', 'greens'],
                                  'Goog': ['tomato', 'cucumber']}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Jon', 'rise')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_len_3(self):
        self.plantation.workers = ['Jon', 'Goog']
        self.plantation.plants = {'Jon': ['popcorn', 'greens'],
                                  'Goog': ['tomato', 'cucumber']}
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Koko', 'rize')
        self.assertEqual("Worker with name Koko is not hired!", str(ex.exception))
        self.assertTrue("Koko" not in self.plantation.workers)

    def test_planting_worker(self):
        self.plantation.workers = ['Jon', 'Goog']
        self.plantation.plants = {'Jon': [], 'Goog': ['tomato']}

        self.assertEqual("Jon planted rise.", self.plantation.planting('Jon', 'rise'))
        self.assertTrue('rise' in self.plantation.plants['Jon'])

    def test_planting_plant(self):
        self.plantation.workers = ['Jon', 'Gogo']
        self.plantation.plants = {'Goog': ['tomato']}
        self.assertEqual("Jon planted it's first rise.", self.plantation.planting('Jon', 'rise'))
        self.assertTrue('rise' in self.plantation.plants['Jon'])


    def test_str(self):
        self.plantation.workers = ['Jon', 'Gogo']
        self.plantation.plants = {'Jon': ['rise'], 'Gogo': ['tomato']}
        result = '''Plantation size: 3
Jon, Gogo
Jon planted: rise
Gogo planted: tomato'''
        self.assertEqual(result, self.plantation.__str__())

    def test_repr(self):
        self.plantation.workers = ['Jon', 'Gogo']
        self.plantation.plants = {'Jon': ['rise'], 'Gogo': ['tomato']}
        result = '''Size: 3
Workers: Jon, Gogo'''
        self.assertEqual(result, self.plantation.__repr__())

if __name__ == "__main__":
    main()