from project_shopping_cart.shopping_cart import ShoppingCart

from unittest import TestCase, main

class TestShopping(TestCase):
    def setUp(self) -> None:
        self.shopping = ShoppingCart('Mani', 50.50)

    def test_init(self):
        self.assertEqual('Mani', self.shopping.shop_name)
        self.assertEqual(50.50, self.shopping.budget)
        self.assertEqual({}, self.shopping.products)

    def test_name_setter(self):
        name = 'manni'
        with self.assertRaises(ValueError)as ex:
            shopping = ShoppingCart(name, 50.50)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_name_setter_2(self):
        name = 'Manna5'
        with self.assertRaises(ValueError)as ex:
            shopping = ShoppingCart(name, 50.50)
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(ex.exception))

    def test_add_to_cart(self):
        with self.assertRaises(ValueError)as ex:
            self.shopping.add_to_cart('dress', 150.00)
        self.assertEqual('Product dress cost too much!', str(ex.exception))

    def test_add_to_cart_2(self):
        with self.assertRaises(ValueError) as ex:
            self.shopping.add_to_cart('dress', 100.00)
        self.assertEqual('Product dress cost too much!', str(ex.exception))

    def test_add_to_cart_3(self):
        result = self.shopping.add_to_cart('dress', 70.00)
        self.assertEqual('dress product was successfully added to the cart!', result)
        self.assertEqual({"dress": 70.00}, self.shopping.products)
        self.assertTrue("dress" in self.shopping.products)

    def test_remove_from_cart(self):
        self.shopping.products = {'dress': 70, 'pants': 40}
        result = self.shopping.remove_from_cart('dress')
        self.assertEqual({'pants': 40}, self.shopping.products)
        self.assertEqual("Product dress was successfully removed from the cart!", result)

    def test_remove_from_cart_1(self):
        self.shopping.products = {'dress': 70, 'pants': 40}
        with self.assertRaises(ValueError)as ex:
            result = self.shopping.remove_from_cart('skirt')
        self.assertEqual("No product with name skirt in the cart!", str(ex.exception))

    def test_add_1(self):
        shopping1 = ShoppingCart('Mani', 50.50)
        shopping1.add_to_cart('skirt', 50.00)
        shopping2 = ShoppingCart('Yavor', 80.00)
        shopping2.add_to_cart('pants', 40.00)
        result = shopping1.__add__(shopping2)
        self.assertEqual('ManiYavor', result.shop_name)
        self.assertEqual(130.50, result.budget)
        self.assertEqual({'skirt': 50.00, 'pants': 40.00}, result.products)

    def test_buy_products(self):
        new_shopping_cart = ShoppingCart('ManiYavor', 130.50)
        new_shopping_cart.add_to_cart('pants', 40.00)
        new_shopping_cart.add_to_cart('skirt', 50.00)
        self.assertEqual('Products were successfully bought! Total cost: 90.00lv.', new_shopping_cart.buy_products())

    def test_buy_products_1(self):
        new_shopping_cart = ShoppingCart('ManiYavor', 70.50)
        new_shopping_cart.add_to_cart('pants', 40.00)
        new_shopping_cart.add_to_cart('skirt', 50.00)
        with self.assertRaises(ValueError)as ex:
            new_shopping_cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 19.50lv!", str(ex.exception))


if __name__ == "__main__":
    main()