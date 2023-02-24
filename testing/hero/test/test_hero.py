from unittest import TestCase, main

from hero.project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero('Harry', 10, 100, 2)
        self.enemy = Hero('Ron', 10, 200, 3)

    def test_init_(self):
        self.assertEqual("Harry", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(2, self.hero.damage)

    def test_str(self):
        expected_result = f"Hero Harry: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 2\n"
        self.assertEqual(expected_result, self.hero.__str__())

    def test_battle_equal_names(self):
        self.enemy.username = "Harry"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_minus_or_0(self):
        self.hero.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_minus_or_0(self):
        self.enemy.health = 0
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Ron. He needs to rest", str(ex.exception))

    def test_draw(self):
        self.hero.damage = 30
        self.enemy.damage = 30
        expected = self.hero.battle(self.enemy)
        self.assertEqual("Draw", expected)

    def test_win(self):
        self.enemy.damage = 1
        self.hero.damage = 110
        self.assertEqual("You win", self.hero.battle(self.enemy))

        self.assertEqual(11,self.hero.level)
        self.assertEqual(95, self.hero.health)
        self.assertEqual(115, self.hero.damage)

    def test_lose(self):
        self.hero.damage = 1
        self.assertEqual("You lose", self.hero.battle(self.enemy))

        self.assertEqual(11, self.enemy.level)
        self.assertEqual(195, self.enemy.health)
        self.assertEqual(8, self.enemy.damage)
