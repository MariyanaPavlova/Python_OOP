from project_1508.product import Product


class Drink(Product):
    def __init__(self, name, quantity=10):
        super().__init__(name, quantity)
