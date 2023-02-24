from horse_race_140822.horse_specification.horse import Horse


class Thoroughbred(Horse):
    max_speed = 140
    def __init__(self, name, speed):
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 137:
            self.speed += 3
        elif self.speed < 140:
            self.speed = 140