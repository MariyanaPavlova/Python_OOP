from project_movie.movie import Movie

from unittest import TestCase, main

class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie('Cingarella', 2015, 5.6)

    def test_init(self):
        self.assertEqual('Cingarella', self.movie.name)
        self.assertEqual(2015, self.movie.year)
        self.assertEqual(5.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_raises(self):
        name = ''
        with self.assertRaises(ValueError) as ex:
            movie = Movie(name, 2015, 5.6)
        self.assertEqual('Name cannot be an empty string!', str(ex.exception))

    def test_year_raises(self):
        with self.assertRaises(ValueError) as ex:
            movie = Movie("Cingarella", 1886, 5.6)
        self.assertEqual('Year is not valid!', str(ex.exception))

    def test_add_actor(self):
        self.movie.actors = []
        self.movie.add_actor('George Kluni')
        self.assertEqual(['George Kluni'], self.movie.actors)
        self.assertTrue("George Kluni" in self.movie.actors)

    def test_add_actor_raises(self):
        self.movie.actors = ['George Kluni']
        self.assertTrue("George Kluni" in self.movie.actors)
        self.assertEqual('George Kluni is already added in the list of actors!', self.movie.add_actor('George Kluni'))
        self.assertEqual(['George Kluni'], self.movie.actors)

    def test_gt_(self):
        self.movie_2 = Movie('Dune', 1993, 7.3)
        self.assertEqual('"Dune" is better than "Cingarella"', self.movie.__gt__(self.movie_2))

        self.movie_2 = Movie('Cingarella2', 2020, 2.3)
        self.assertEqual('"Cingarella" is better than "Cingarella2"', self.movie.__gt__(self.movie_2))


    def test_repr_(self):
        self.movie.actors = ["Name1, Name2"]
        result = '''Name: Cingarella
Year of Release: 2015
Rating: 5.60
Cast: Name1, Name2'''

        self.assertEqual(result, self.movie.__repr__())

if __name__ == "__main__":
    main()