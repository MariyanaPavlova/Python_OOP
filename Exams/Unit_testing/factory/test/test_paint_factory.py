from project_plantation.factory.paint_factory import PaintFactory

from unittest import TestCase, main

class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('Mama', 5)

    def test_init_(self):
        factory = PaintFactory('Mama', 5)

        self.assertEqual('Mama', factory.name)
        self.assertEqual(5, factory.capacity)
        self.assertEqual({}, factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], factory.valid_ingredients)

    def test_can_add(self):
        self.factory.can_add(2)
        result = 3 >=0
        self.assertEqual(result, self.factory.can_add(2))

        self.factory.can_add(6)
        result = -1 >= 0
        self.assertEqual(result, self.factory.can_add(6))

    def test_add_ingredients_raise_error(self):
        with self.assertRaises(ValueError) as ex:
            self.factory.add_ingredient('white', 35)
        self.assertEqual("Not enough space in factory", str(ex.exception))

        with self.assertRaises(TypeError) as ex:
            self.factory.add_ingredient('pink', 2)
        self.assertEqual("Ingredient of type pink not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredients(self):
        ingredients = {'white': 2}
        result = self.factory.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.factory.ingredients)
        self.assertTrue("white" in self.factory.ingredients)

        ingredients = {'white': 1}
        result = self.factory.add_ingredient('white', 1)
        self.assertEqual({'white': 3}, self.factory.ingredients)

    def test_remove_ingredient(self):
        self.ingredients = {'white': 2}

        self.factory.add_ingredient('white', 2)
        result = self.factory.remove_ingredient('white', 2)
        self.assertTrue("white" in self.factory.ingredients)
        self.assertEqual({'white': 0}, self.factory.ingredients)

    def test_remove_ingredient_raise_error(self):
        self.factory.add_ingredient('white', 2)
        with self.assertRaises(ValueError) as ex:
            self.factory.remove_ingredient('white', 5)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_raise_error_1(self):
        self.factory.add_ingredient('white', 2)
        with self.assertRaises(KeyError) as ex:
            self.factory.remove_ingredient('pink', 1)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_repr(self):
        self.factory.add_ingredient('white', 2)
        self.factory.add_ingredient('green', 2)
        result = """Factory name: Mama with capacity 5.
white: 2
green: 2"""
        self.assertEqual(result, self.factory.__repr__())


if __name__ == '__main__':
    main()