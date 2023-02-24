from horse_race_140822.horse_race import HorseRace
from horse_race_140822.horse_specification.appaloosa import Appaloosa
from horse_race_140822.horse_specification.thoroughbred import Thoroughbred
from horse_race_140822.jockey import Jockey


class HorseRaceApp:
    _valid_horse_type = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses = []  #obj
        self.jockeys = []  #obj
        self.horse_races = [] #obj


    def _find_last_horse(self, horse_type):
        last_horse = None
        if horse_type in self._valid_horse_type:
            for horse in self.horses:
             if horse.__class__.__name__== horse_type:
                last_horse = horse
        return last_horse

    def _find_jockey(self, jockey_name):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def _find_horse_race(self, race_type):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return horse_race

    #добавяме кон
    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
                          #връща името
        #if horse_name in [h.name for h in self.horses]
        if horse_type in self._valid_horse_type:
            for horse in self.horses:
                if horse.name == horse_name:
                    return f"Horse {horse_name} has been already added!"

            new_horse = self._valid_horse_type[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    #добавяме жокей
    def add_jockey(self, jockey_name: str, age: int):
                        #връща   името
        #if jockey_name in [j.name for j in self.jockeys]
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return f"Jockey {jockey_name} has been already added!"

        new_jokey = Jockey(jockey_name, age)
        self.jockeys.append(new_jokey)
        return f"Jockey {jockey_name} is added."

    #добавяме хорсе рейс
    def create_horse_race(self, race_type: str):
        for horse_race in self.horse_races:
            if horse_race.race_type == race_type:
                return f"Race {race_type} has been already created!"

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        free_horse = self._find_last_horse(horse_type)
        free_jockey = self._find_jockey(jockey_name)

        if not free_horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if not free_jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

    #може и така
        if free_jockey.horse:
            return f"Jockey {jockey_name} already has a horse."
        else:
            free_jockey.horse = free_horse
            free_horse.is_taken = True
            return f"Jockey {jockey_name} will ride the horse {free_horse.name}."
        #вместо
        # for jockey in self.jockeys:
        #     if jockey.horse is not None and jockey.name == jockey_name:
        #         return f"Jockey {jockey_name} already has a horse."
        #
        #     elif jockey.horse is None and jockey.name == jockey_name:
        #         jockey.horse = free_horse
        #         jockey.horse.is_taken = True
        #         return f"Jockey {jockey_name} will ride the horse {free_jockey.horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        free_jockey = self._find_jockey(jockey_name)
        race = self._find_horse_race(race_type)

        if not free_jockey:
            raise Exception(f'Jockey {jockey_name} could not be found!')
        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if not free_jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

    # може и така
        if free_jockey in race.jockey:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."
        else:
            race.jockey.append(free_jockey)
            return f'Jockey {jockey_name} added to the {race_type} race.'
       #вместо
        # for r in self.horse_races:
        #     for j in r.jockeys:
        #         if j.name == jockey_name:
        #             return f"Jockey {jockey_name} has been already added to the {race_type} race."
        #     else:
        #         self.horse_races.append(horse_race.jockeys.append(free_jockey))
        #         return f'Jockey {jockey_name} added to the {race_type} race.'
        #

    def start_horse_race(self, race_type: str):
        race = self._find_horse_race(race_type)

        if not race:
            raise Exception(f"Race {race_type} could not be found!")
        if len(race.jockey) <2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        the_fastest_jockey = sorted(race.jockey, key=lambda jockey: -jockey.horse.speed)[0]

        # може и така
        # highest_speed = 0
        # winner = None
        # for jockey in horse_rase.jockeys:
        #     if jockey.horse.speed > highest_speed:
        #         highest_speed = jockey.horse.speed
        #         winner = jockey
        return f"The winner of the {race_type} race, with a speed of {the_fastest_jockey.horse.speed}km/h is {the_fastest_jockey.name}! Winner's horse: {the_fastest_jockey.horse.name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))

