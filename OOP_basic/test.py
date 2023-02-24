class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calc_total_price(self, x, y):
        return x * y

item1 = Item("phone", 100, 5)
item2 = Item('laptop', 1000,3)
print()