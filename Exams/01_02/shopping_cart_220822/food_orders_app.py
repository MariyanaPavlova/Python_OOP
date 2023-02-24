from shopping_cart_220822.client import Client
from shopping_cart_220822.meals.meal import Meal

from shopping_cart_220822.meals.starter import Starter
from shopping_cart_220822.meals.dessert import Dessert
from shopping_cart_220822.meals.main_dish import MainDish


class FoodOrdersApp:
    _valid_meals = {"Starter":Starter, "MainDish":MainDish, "Dessert":Dessert}
    receipt_id = 0

    def __init__(self):
        self.menu = [] #Obj
        self.clients_list = [] #Obj


    def register_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for m in meals:
            if m.__class__.__name__ in self._valid_meals:
                self.menu.append(m)

    def show_menu(self):
        if len(self.menu) <5:
            raise Exception("The menu is not ready!")
        string = ''
        for el in self.menu:
            string += el.details() + "\n"
        return string.strip()

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) <5:
            raise Exception("The menu is not ready!")

        client = self.__find_client(client_phone_number)
        meals_to_order = []
        current_bill = 0

        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                for m, v in meal_names_and_quantities.items():
                    for el in self.menu:
                        if m == el.name:
                            if el.quantity >= v:
                                el.quantity -= v
                                meals_to_order.append(el)
                                current_bill += el.price * v
                            else:
                                raise Exception(f"Not enough quantity of {el.__class__.__name__}: {m}!")
                # else:
                #     raise Exception(f"{m} is not on the menu!")

            else:
                self.register_client(client_phone_number)
                for m, v in meal_names_and_quantities.items():
                   for el in self.menu:
                        if m == el.name:
                            if el.quantity >= v:
                                el.quantity -= v
                                meals_to_order.append(el)
                                current_bill += el.price * v
                            else:
                                raise Exception(f"Not enough quantity of {el.__class__.__name__}: {m}!")
                else:
                    raise Exception(f"{m} is not on the menu!")

        client.shopping_cart.extend(meals_to_order)
        client.bill += current_bill

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join(meal.name for meal in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        client.shopping_cart = []
        client.bill = 0
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.__find_client(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception(f"There are no ordered meals!")

        else:
            self.receipt_id += 1
            shop_cart = client.shopping_cart
            client.shopping_cart = []
            bill = client.bill
            client.bill = 0
            return f"Receipt #{self.receipt_id} with total amount of {bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


    def __find_client(self, client_phone_number: str):
        for client in self.clients_list:
            if client.phone_number == client_phone_number:
                return client

food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))

additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)