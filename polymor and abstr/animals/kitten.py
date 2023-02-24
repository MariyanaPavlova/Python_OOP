from project_1508.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')

    def make_sound(self):
        return "Meow"
