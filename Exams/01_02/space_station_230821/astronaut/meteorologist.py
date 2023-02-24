from space_station_230821.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15
        