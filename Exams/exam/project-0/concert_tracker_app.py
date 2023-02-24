from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.musician import Musician
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    valid_types = {"Guitarist":Guitarist, "Drummer":Drummer, "Singer":Singer}

    def __init__(self):
        self.bands = [] #obj
        self.musicians = [] #obj
        self.concerts = [] #obj

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.valid_types:
            raise ValueError("Invalid musician type!")

        for m in self.musicians:
            if musician_type == m.__class__.__name__:
                raise Exception(f"{name} is already a musician!")

        musicant = self.valid_types[musician_type](name, age)
        self.musicians.append(musicant)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        for n in self.bands:
            if n.name == name:
                raise Exception(f"{name} band is already created!")

        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        for c in self.concerts:
            if c.place == place:
                return f"{place} is already registered for {genre} concert!"


        new_concet = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concet)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        found_mus = self._find_musicians(musician_name)
        if not found_mus:
            raise Exception(f"{musician_name} isn't a musician!")

        found_band = self._find_band(band_name)
        if not found_band:
            raise Exception(f"{band_name} isn't a band!")

        if found_band and found_mus:
            found_band.members.append(found_mus)
            return f"{musician_name} was added to {band_name}."

    def _find_musicians(self, musician_name):
        for mus in self.musicians:
            if mus.name == musician_name:
                return mus

    def _find_band(self, band_name):
        for b in self.bands:
            if b.name == band_name:
                return b

    def __find_concert(self, concert_place):
        for c in self.concerts:
            if c.place == concert_place:
                return c

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        found_band = self._find_band(band_name)
        if not found_band:
            raise Exception(f"{band_name} isn't a band!")

        found_mus = self._find_musicians(musician_name)
        if not found_mus:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        if found_band and found_mus:
            found_band.members.remove(found_mus)
            return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        found_band = self._find_band(band_name)
        member = []
        for band in self.bands:
            for i in band.members:
                if i.__class__.__name__ in self.valid_types:
                    member.append(i.__class__.__name__)
        if len(member) < 3:
            return f"{band_name} can't start the concert because it doesn't have enough members!"

        concet = self.__find_concert(concert_place)
        profit = concet.audience * concet.ticket_price - concet.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concet.genre} concert in {concert_place}."


musician_types = ["Singer", "Drummer", "Guitarist"]
names = ["George", "Alex", "Lilly"]

app = ConcertTrackerApp()

for i in range(3):
    print(app.create_musician(musician_types[i], names[i], 20))

print(app.musicians[0].learn_new_skill("sing high pitch notes"))
print(app.musicians[1].learn_new_skill("play the drums with drumsticks"))
print(app.musicians[2].learn_new_skill("play rock"))

print(app.create_band("RockName"))
for i in range(3):
    print(app.add_musician_to_band(names[i], "RockName"))

print(app.create_concert("Rock", 20, 5.20, 56.7, "Sofia"))

print(list(map(lambda a: a.__class__.__name__, app.bands[0].members)))
print(app.start_concert("Sofia", "RockName"))