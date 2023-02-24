class Vehicle:
    def __init__(self, mileage, max_speed = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []



car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
car2 = Vehicle(200)
print(car2.max_speed)
print(car2.mileage)
print(car2.gadgets)
car2.gadgets.append('Hudly Wireless2')
print(car2.gadgets)