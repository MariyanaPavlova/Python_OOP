from abc import abstractmethod, ABC

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return 'Meow'

class Dog(Animal):
    def make_sound(self):
        return 'Wolf'

class Chicken(Animal):
    def make_sound(self):
        return 'Peow'

class Pig(Animal):
    def make_sound(self):
        return 'Cruh'

def animal_sound(animals: list):
    for i in animals:
        print(i.make_sound())


animals = [Cat(), Dog(), Chicken(), Pig()]
animal_sound(animals)