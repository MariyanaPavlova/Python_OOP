from abc import ABC, abstractmethod

from acquirium_100421.decoration.base_decoration import BaseDecoration
from acquirium_100421.fish.base_fish import BaseFish
from acquirium_100421.fish.freshwater_fish import FreshwaterFish
from acquirium_100421.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(ABC):
    _possible_fish = {"FreshwaterFish": FreshwaterFish, "SaltwaterFish": SaltwaterFish}
    @abstractmethod
    def __init__(self, name:str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []  #dec obj
        self.fish = [] #all fish obj


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f"Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum(dec.comfort for dec in self.decorations)

    def add_fish(self, fish:BaseFish):
        if len(self.fish) < self.capacity and fish.__class__.__name__ in self._possible_fish[fish]:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        return f"Not enough capacity."

    def remove_fish(self, fish:BaseFish):
        self.fish.remove(fish)

    def add_decoration(self, decoration:BaseDecoration):
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        fishes = "none" if len(self.fish) == 0 else ", ".join([fish.name for fish in self.fish])
        return f'''{self.name}:
Fish: {fishes}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}'''