from space_station_230821.astronaut.astronaut_repository import AstronautRepository
from space_station_230821.planet.planet_repository import PlanetRepository
from space_station_230821.astronaut.biologist import Biologist
from space_station_230821.astronaut.geodesist import Geodesist
from space_station_230821.astronaut.meteorologist import Meteorologist
from space_station_230821.planet.planet import Planet


class SpaceStation:
    _valid_types = {'Biologist': Biologist, 'Geodesist': Geodesist, 'Meteorologist': Meteorologist}

    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.astronauts_high_oxygen = []
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in self._valid_types:
            raise Exception("Astronaut type is not valid!")

        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is not None:
            return f'{name} is already added.'

        self.astronaut_repository.add(self._valid_types[astronaut_type](name))
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet is not None:
            return f'{name} is already added.'

        planet = Planet(name)
        planet.items = items.split(", ")
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'


    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is not None:
            self.astronaut_repository.remove(astronaut)
            return f'Astronaut {name} was retired!'
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception('Invalid planet name!')

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                self.astronauts_high_oxygen.append(astronaut)

        if len(self.astronauts_high_oxygen) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts_high_oxygen = sorted(self.astronauts_high_oxygen, key=lambda  x: x.oxygen, reverse=True)[0:5]

        part = 0
        for astronaut in sorted_astronauts_high_oxygen:
            if len(planet.items) ==0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            part +=1

        if len(planet.items) == 0:
            self.successful_missions +=1
            return f'Planet: {planet_name} was explored. {part} astronauts participated in collecting items.'
        else:
            self.failed_missions += 1
            return f'Mission is not completed.'


    def report(self):
        result = f'{self.successful_missions} successful missions!' + "\n"
        result += f'{self.failed_missions} missions were not completed!' + "\n"
        result += "Astronauts' info:" + "\n"

        for asronaut in self.astronaut_repository.astronauts:
            result += str(asronaut) + "\n"

        return result.strip()



sp_station = SpaceStation()

print(sp_station.add_astronaut("Biologist", "1"))
print(sp_station.add_astronaut("Geodesist", "Pe"))
print(sp_station.add_astronaut("Meteorologist", "2"))

print(sp_station.add_planet("Earth", "item1, st6"))
print(sp_station.send_on_mission("Earth"))
print(sp_station.report())