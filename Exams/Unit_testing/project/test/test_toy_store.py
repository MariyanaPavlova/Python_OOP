from project.toy_store import ToyStore


from unittest import TestCase, main

class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.toystory = ToyStore()

    def test_init_(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
, self.toystory.toy_shelf)

    def test_add_toy(self):
        with self.assertRaises(Exception) as ex:
            self.toystory.add_toy("ff", "track")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_(self):
        self.toystory.toy_shelf={
            "A": "track",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.toystory.add_toy("A", "track")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_3(self):
        self.toystory.toy_shelf={
            "A": "track",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        with self.assertRaises(Exception) as ex:
            self.toystory.add_toy("A", "dol")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_add_toy_4(self):
        self.toystory.toy_shelf={
            "A": "track",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        result = self.toystory.add_toy("B", "doll")
        self.assertEqual("Toy:doll placed successfully!", result)
        self.assertEqual({
            "A": "track",
            "B": "doll",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystory.toy_shelf)


    def test_remove_toy(self):
        with self.assertRaises(Exception) as ex:
            self.toystory.remove_toy("ff", "track")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_1(self):
        self.toystory.toy_shelf = {
            "A": "track",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toystory.remove_toy("A", "doll")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_toy_2(self):
        self.toystory.toy_shelf = {
            "A": "track",
            "B": "doll",
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.toystory.remove_toy("B", "doll")
        self.assertEqual("Remove toy:doll successfully!", result)
        self.assertEqual({
            "A": "track",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toystory.toy_shelf)


if __name__ == "__main__":
    main()