from car_race_111221.car.car import Car


class MuscleCar(Car):
    _MIN_SPEED = 250
    _MAX_SPEED = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)