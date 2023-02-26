from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Fluffy", "Cat", 'Meow')

    def test_mammal_init(self):
        mammal = Mammal("Fluffy", "Cat", 'Meow')

        self.assertEqual(mammal.name, "Fluffy")
        self.assertEqual(mammal.type, 'Cat')
        self.assertEqual(mammal.sound, "Meow")
        self.assertEqual(mammal._Mammal__kingdom, "animals")

    def test_make_sound_proper_result(self):
        #mammal = Mammal("Fluffy", "Cat", 'Meow')

        actual_result = self.mammal.make_sound()
        expected_result = f"Fluffy makes Meow"

        self.assertEqual(actual_result, expected_result)

    def test_get_kingdom_returns_animals(self):
        # mammal = Mammal("Fluffy", "Cat", 'Meow')

        actual_result = self.mammal.get_kingdom()
        expected_result = 'animals'

        self.assertEqual(actual_result, expected_result)

    def test_info(self):
        # mammal = Mammal("Fluffy", "Cat", 'Meow')

        actual_result = self.mammal.info()
        expected_result = f"Fluffy is of type Cat"

        self.assertEqual(actual_result, expected_result)

if __name__ == "main":
    main()



