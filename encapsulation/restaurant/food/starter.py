from project_1508.food.food import Food


class Starter(Food):
    def __init__(self, name, price, grams):
        super().__init__(name, price, grams)
