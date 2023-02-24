from acquirium_100421.aquarium.base_aquarium import BaseAquarium
from acquirium_100421.aquarium.freshwater_aquarium import FreshwaterAquarium
from acquirium_100421.aquarium.saltwater_aquarium import SaltwaterAquarium
from acquirium_100421.decoration.decoration_repository import DecorationRepository
from acquirium_100421.decoration.ornament import Ornament
from acquirium_100421.decoration.plant import Plant
from acquirium_100421.fish.freshwater_fish import FreshwaterFish
from acquirium_100421.fish.saltwater_fish import SaltwaterFish


class Controller:
    _possible_fish = {"FreshwaterFish":FreshwaterFish, "SaltwaterFish":SaltwaterFish}
    _acq_types = {"FreshwaterAquarium":FreshwaterAquarium, "SaltwaterAquarium":SaltwaterAquarium}
    _dec_types = {"Ornament":Ornament, "Plant":Plant}

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []  #acq obj

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type in self._acq_types:


        acquarium = self._acq_types[aquarium_type](aquarium_name, aquarium_type)
        self.aquariums.append(acquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self._dec_types:
            return f"Invalid decoration type."

        decoration = self._dec_types[decoration_type]()
        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        decor = self.decorations_repository.find_by_type(decoration_type)
        acq = self.find_acquarium_by_name(aquarium_name)

        if decor and acq:
            self.decorations_repository.remove(decor)
            acq.add_decoration(aquarium_name)
            return f"Successfully added {decoration_type} to {aquarium_name}."

        elif not decor:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        pass

    def feed_fish(self, aquarium_name: str):
        pass

    def calculate_value(self, aquarium_name: str):
        pass

    def report(self):
        pass

    def find_acquarium_by_name(self, aquarium_name):
        for acquarium in self.aquariums:
            if acquarium.name == aquarium_name:
                return acquarium
