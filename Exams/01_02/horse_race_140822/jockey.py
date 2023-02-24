class Jockey:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
        self.horse = None   #obj


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f"Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError(f'Jockeys must be at least 18 to participate in the race!')
        self.__age = value