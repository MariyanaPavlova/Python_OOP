from project_1508.food import Food
from project_1508.drink import Drink

class ProductRepository():

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name):
        #product = self.find(product_name)
        #if product is not None:
        #self.products.remove(product)
        for obj in self.products:
            if obj.name == product_name:
                self.products.remove(obj)
                break

    def __repr__(self):
        res = ""
        for i in self.products:
            res += f'{i.name}: {i.quantity}\n'
        return res.strip()


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)