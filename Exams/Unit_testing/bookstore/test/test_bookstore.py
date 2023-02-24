from project_bookstore.bookstore import Bookstore

from unittest import TestCase, main

class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(5)

    def test_init_(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_limit_setter(self):
        with self.assertRaises(ValueError)as ex:
            bookstore = Bookstore(-1)
        self.assertEqual("Books limit of -1 is not valid", str(ex.exception))

    def test_limit_setter_0(self):
        with self.assertRaises(ValueError)as ex:
            bookstore = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ex.exception))

    def test_len_0(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 0, "Book2": 0}
        self.assertEqual(0, self.bookstore.__len__())

    def test_len_1(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}
        self.assertEqual(3, self.bookstore.__len__())


    def test_receive_book_raise(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}
        with self.assertRaises(Exception)as ex:
            self.bookstore.receive_book('Book3', 5)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book__equal_book_limit(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 1, "Book2": 2}
        result = self.bookstore.receive_book('Book1', 2)
        self.assertEqual('3 copies of Book1 are available in the bookstore.', result)
        self.assertEqual(3, self.bookstore.availability_in_store_by_book_titles['Book1'])

    def test_receive_book_1(self):
        self.bookstore.availability_in_store_by_book_titles = {"Book1": 1}
        result = self.bookstore.receive_book('Book1', 1)
        self.assertEqual('2 copies of Book1 are available in the bookstore.', result)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles['Book1'])

    def test_receive_book_2(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 1}
        result = self.bookstore.receive_book('Book2', 1)
        self.assertEqual({'Book1': 1, 'Book2': 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual('1 copies of Book2 are available in the bookstore.', result)


    def test_sell_book(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 1}
        with self.assertRaises(Exception)as ex:
            self.bookstore.sell_book('Book2', 5)
        self.assertEqual("Book Book2 doesn't exist!", str(ex.exception))

    def test_sell_book_2(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 3}
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book('Book1', 6)
        self.assertEqual("Book1 has not enough copies to sell. Left: 3", str(ex.exception))

    def test_sell_book_3(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 3}
        result = self.bookstore.sell_book('Book1', 2)
        self.assertEqual(1, self.bookstore.availability_in_store_by_book_titles['Book1'])
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual('Sold 2 copies of Book1', result)

    def test_sell_book__equal_book_limit(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 5}
        result = self.bookstore.sell_book('Book1', 5)
        self.assertEqual(0, self.bookstore.availability_in_store_by_book_titles['Book1'])
        self.assertEqual(5, self.bookstore.total_sold_books)
        self.assertEqual('Sold 5 copies of Book1', result)

    def test_str_(self):
        self.bookstore.availability_in_store_by_book_titles = {'Book1': 3}
        self.bookstore.sell_book('Book1', 2)

        result = '''Total sold books: 2
Current availability: 1
 - Book1: 1 copies'''

        self.assertEqual(result, self.bookstore.__str__())


if __name__ == '__main__':
    main()