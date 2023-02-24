from project_1508.animals import Animal


class Cheetah(Animal):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, 60)