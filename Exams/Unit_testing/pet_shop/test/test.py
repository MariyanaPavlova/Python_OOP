from unittest import TestCase, main
from project_pet_shop.pet_shop import PetShop

class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('PetShop')

    def test_init(self):
        name = "PetShop"
        pet_shop = PetShop(name)

        self.assertEqual(name, pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_add_food_1(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food('Pesho', -25)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_2(self):
        food_name = 'food1'
        food_quantity = 50
        result = self.pet_shop.add_food(food_name, food_quantity)
        self.assertEqual("Successfully added 50.00 grams of food1.", result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(50, self.pet_shop.food[food_name])

    def test_add_food_3(self):
        food_name = "food1"
        food_quantity = 100
        result = self.pet_shop.add_food(food_name, food_quantity)
        result = self.pet_shop.add_food(food_name, food_quantity)

        self.assertEqual("Successfully added 100.00 grams of food1.", result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(200, self.pet_shop.food["food1"])

    def test_add_pet_1(self):
        pet_name = "pet1"
        self.pet_shop.pets.append(pet_name)
        pet_name = "pet1"
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet(pet_name)
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet_2(self):
        pet_name = "pet1"
        res = self.pet_shop.add_pet(pet_name)

        self.assertEqual('Successfully added pet1.', res)
        self.assertTrue("pet1" in self.pet_shop.pets)

    def test_feed_pet_1(self):
        self.pet_shop.add_pet("Bono")
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Ron", "fish")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_2(self):
        self.pet_shop.pets.append("Bono")
        self.pet_shop.food['Bono'] = 'granuli'

        res = self.pet_shop.feed_pet("meat", "Bono")
        self.assertEqual('You do not have meat', res)

    def test_feed_pet_3(self):
        pet_name = "Matsa"
        self.pet_shop.add_pet(pet_name)
        food_name = "fish"
        food_quantity = 50
        self.pet_shop.add_food(food_name, food_quantity)

        res = self.pet_shop.feed_pet("fish", 'Matsa')
        self.assertEqual(1050, self.pet_shop.food['fish'])
        self.assertEqual("Adding food...", res)

    def test_feed_pet_4(self):
        pet_name = "Matsa"
        self.pet_shop.pets.append(pet_name)
        food_name = "fish"
        food_quantity = 500
        self.pet_shop.food[food_name] = food_quantity

        res = self.pet_shop.feed_pet("fish", 'Matsa')
        self.assertEqual(400, self.pet_shop.food[food_name])
        self.assertEqual("Matsa was successfully fed", res)

    def test_repr(self):
        self.pet_shop.pets.append('Bono')
        self.pet_shop.pets.append('Matsa')
        result = repr(self.pet_shop)
        actual = 'Shop PetShop:\n' 'Pets: Bono, Matsa'
        self.assertEqual(actual, result)


if __name__ == "__main__":
    main()