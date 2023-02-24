class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):  #правим функ.връщаща инфо
        return f'Book title {self.title} {self.author}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        try:
            return [book for book in self.books if book.title == title][0]
        except IndexError:
            return "Book not found"

library = Library()

for i in range(1, 21):
    book = Book(f'Title {i}', f'Autor {i}')
    library.add_book(book)

print(library.find_book(f'Title 1'))  #връща <__main__.Book object at 0x7f00bda75310>
                                    #затова ползваме __str__
print(library.__repr__)