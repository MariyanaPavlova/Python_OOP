from project_1508.baked_food.bread import Bread
from project_1508.baked_food.cake import Cake
from project_1508.drink.tea import Tea
from project_1508.drink.water import Water


class FoodFactory:
    #food_types = {"Cake": Cake, "Bread": Bread}

    def create_food(self, food_type, name, price):
        if food_type == "Cake":
            return Cake(name, price)
        if food_type == "Bread":
            return Bread(name, price)

    #def create_food(self, food_type, name, price):
        #return self.__class__.food_types[food_type](name, price)


class DrinkFactory:
    def create_drink(self, drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        if drink_type == "Water":
            return Water(name, portion, brand)

