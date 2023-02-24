from inheritance.project_0_food.food import Food


class Fruit(Food):
    def __init__(self, name, expiration_date):
        self.name = name
        super().__init__(expiration_date)
        super().__str__()

fruit = Fruit('apple', '2020-01')
print(fruit.name, fruit.expiration_date)