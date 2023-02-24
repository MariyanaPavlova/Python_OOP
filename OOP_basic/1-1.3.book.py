class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

book = Book("My Book", "Me", 200)
print(book)
print(book.name)
print(book.author)
print(book.pages)


****
class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

car = Car("Kia", "Rio", "1.3L B3 I4")

print(car.get_info())