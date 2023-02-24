class Mammal:
    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.type = mammal_type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"


from unittest import TestCase, main


class TestMammal(TestCase):
    def setUp(self) -> None:
        name = "Peter"
        type = "Mammal Type"
        sound = 'sound'
        self.mammal = Mammal(name, type, sound)

    def test_mammal_init(self):
        # name = "Peter"
        # type = "Mammal Type"
        # sound = 'sound'
        # mammal = Mammal(name, type, sound)

        self.assertEqual(self.mammal.name, "Peter")
        self.assertEqual(self.mammal.type, 'Mammal Type')
        self.assertEqual(self.mammal.sound, "sound")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")


    def test_make_sound(self):
        # name = "Peter"
        # mammal_type = "Mammal Type"
        # sound = 'sound'
        # mammal = Mammal(name, mammal_type, sound) и отдолу без self.
        expected_result = f"{self.mammal.name} makes {self.mammal.sound}"
        actual_result = self.mammal.make_sound()

        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom_returns_animals(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info_result(self):
        expected_result = f"{self.mammal.name} is of type {self.mammal.type}"
        actual_result = self.mammal.info()

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    main()