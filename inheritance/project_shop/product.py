class Product:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, new_quantity):
        if self.quantity >= new_quantity:
            self.quantity -= new_quantity

    def increase(self, final_quantity):
        self.quantity += final_quantity

    def __repr__(self):
        return self.name
