from project_library.library import Library

from unittest import TestCase, main

class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('MM')

    def test_init(self):
        library_name = 'MM'
        library = Library(library_name)

        self.assertEqual(library_name, library.name)
        self.assertEqual({}, library.books_by_authors)
        self.assertEqual({}, library.readers)

    def test_raises(self):
        library_name = ''

        with self.assertRaises(ValueError) as ex:
            library = Library(library_name)
        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book(self):
        books_by_author = {}
        books_by_author['Steven King'] = ["Dead zone"]
        result = self.library.add_book("Steven King", "Dead zone")

        self.assertEqual(books_by_author, self.library.books_by_authors)
        self.assertTrue("Steven King" in self.library.books_by_authors)

    def test_add_book_1(self):
        books_by_author = {'Steven King': ["Dead zone"]}
        self.library.add_book("Steven King", "Dead zone")

        self.assertEqual(books_by_author, self.library.books_by_authors)
        self.assertTrue("Steven King" in self.library.books_by_authors)

    def test_add_reader_1(self):
        readers = {}
        readers['Yavor'] = []
        self.library.add_reader("Yavor")

        self.assertEqual(readers, self.library.readers)
        self.assertTrue('Yavor' in self.library.readers)

    def test_add_reader_2(self):
        readers = {'Yavor': []}
        self.library.add_reader("Yavor")

        self.assertEqual("Yavor is already registered in the MM library.", self.library.add_reader(('Yavor')))
        self.assertEqual({"Yavor":[]}, self.library.readers)

    def test_rent_book_1(self):
        readers = {'Yavor': []}
        books_by_authors = {'Steven King': ["Dead zone"]}
        result = self.library.rent_book('Mama', 'Maria Laleva', 'Life')

        self.assertEqual('Mama is not registered in the MM Library.', result)
        self.assertTrue('Mama' not in self.library.readers)

    def test_rent_book_2(self):
        readers = {'Yavor': []}
        books_by_authors = {'Steven King': ["Dead zone"]}

        self.library.add_reader('Yavor')
        result = self.library.rent_book('Yavor', 'Maria Laleva', 'Life')

        self.assertEqual("MM Library does not have any Maria Laleva's books.", result)

    def test_rent_book_3(self):
        readers = {'Yavor': []}
        books_by_authors = {'Steven King': ["Dead zone"]}

        self.library.add_reader('Yavor')
        self.library.add_book("Steven King", "Dead zone")
        result = self.library.rent_book('Yavor', 'Steven King', 'Life')

        self.assertEqual("""MM Library does not have Steven King's "Life".""", result)

    def test_rent_book_4(self):
        readers = {'Yavor': []}
        books_by_authors = {'Steven King': ["Dead zone"]}
        readers = {'Yavor': [{'Steven King': "Dead zone"}]}

        self.library.add_reader('Yavor')
        self.library.add_book("Steven King", "Dead zone")
        result = self.library.rent_book('Yavor', 'Steven King', 'Dead zone')

        self.assertEqual(readers, self.library.readers)

    def test_rent_book_5(self):
        readers = {'Yavor': []}
        books_by_authors = {'Steven King': ["Dead zone"]}
        readers = {'Yavor': [{'Steven King': "Dead zone"}]}
        books_by_authors = {'Steven King': []}

        self.library.add_reader('Yavor')
        self.library.add_book("Steven King", "Dead zone")
        self.library.rent_book('Yavor', 'Steven King', 'Dead zone')

        self.assertEqual(books_by_authors, self.library.books_by_authors)
        self.assertTrue('Dead zone' not in self.library.books_by_authors)


if __name__ == "__main__":
    main()
