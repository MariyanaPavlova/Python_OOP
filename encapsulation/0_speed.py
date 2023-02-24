class Car:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        print('drive ' + str(self.speed))

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > 447:
            value = 447
        self.__speed = value

red_car = Car(200)
red_car.drive()
red_car.speed = 512
red_car.drive()
print(red_car.speed)
