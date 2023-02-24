from car_race_111221.car.car import Car
from car_race_111221.car.muscle_car import MuscleCar
from car_race_111221.car.sports_car import SportsCar
from car_race_111221.driver import Driver
from car_race_111221.race import Race


class Controller:
    _valid_car_models = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars = []      #obj cars
        self.drivers = []     #obj drivers
        self.races = []     #obj races


    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in self._valid_car_models:
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")

            #car е абстр.затова през речника взимам типа за името на класа
            car = self._valid_car_models[car_type](model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."


    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):

        driver_in = [driver for driver in self.drivers if driver_name == driver.name]
        if not driver_in:
            raise Exception(f"Driver {driver_name} could not be found!")

        free_car = [car for car in self.cars if car.is_taken == False and car.__class__.__name__ == car_type]
        if not free_car:
            raise Exception(f'Car {car_type} could not be found!')

        if driver_in and free_car:
            car = free_car.pop()
            for driver in self.drivers:
                if driver.car == None:
                    car.is_taken = True
                    driver.car = car
                    return f"Driver {driver_name} chose the car {car.model}."
                else:
                    car.is_taken = True
                    old_model = driver.car.model
                    driver.car = car
                    return f"Driver {driver_name} changed his car from {old_model} to {car.model}."


    def add_driver_to_race(self, race_name: str, driver_name: str):
        race_in = [race for race in self.races if race.name == race_name]
        if not race_in:
            raise Exception(f"Race {race_name} could not be found!")

        driver_in = [driver for driver in self.drivers if driver_name == driver.name]
        if not driver_in:
            raise Exception(f"Driver {driver_name} could not be found!")

        for driver in self.drivers:
            if driver.car:
                raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        pass


# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# # print(controller.add_car_to_driver("Jack", "MuscleCar"))
# # print(controller.add_car_to_driver("John", "SportsCar"))
# # print(controller.create_race("Christmas Top Racers"))