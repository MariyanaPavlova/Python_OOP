from horse_race_140822.horse_specification.horse import Horse


class Appaloosa(Horse):
    max_speed = 120
    def __init__(self, name: str, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        elif self.speed < 120:
            self.speed = 120