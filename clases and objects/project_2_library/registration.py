from project_1508.library import Library
from project_1508.user import User


class Registration:

    def add_user(self, user: User, library: Library):
        for i in library.user_records:
            if i.user_id == user.user_id:
                return f'User with id = {user.user_id} already registered in the library!'

        library.rented_books.append(user)
        library.rented_books[user.username] = {}

    def remove_user(user: User, library: Library):
        for i in library.user_records:
            if i.user_id == user.user_id:
                library.user_records.remove(user)
                library.rented_books.pop(user.username)
                return
        return "We could not find such user to remove!"

    def change_username(self, user_id:int, new_username:str, library: Library):
        for i in library.user_records:
            if i.user_id != user_id:
                continue
            if i.user_id == new_username:
                return f"Please check again the provided username - it should be different than the username used so far!"
            i.username = new_username
            rented_books = library.rented_books[i.username]
            library.rented_books.pop(i.username)
            library.rented_books[new_username] = rented_books
            return f"Username successfully changed to: {new_username} for user id: {user_id}"
        return f"There is no user with id = {user_id}!"


from project_1508.library import Library
from project_1508.user import User
from project_1508.registration import Registration

user = User(12, 'Peter')
library = Library()
registration = Registration()
registration.add_user(user, library)
print(registration.add_user(user, library))
registration.remove_user(user, library)
print(registration.remove_user(user, library))
registration.add_user(user, library)
print(registration.change_username(2, 'Igor', library))
print(registration.change_username(12, 'Peter', library))
print(registration.change_username(12, 'George', library))

[print(f'{user_record.user_id}, {user_record.username}, {user_record.books}') for user_record in library.user_records]

library.books_available.update({'J.K.Rowling': ['The Chamber of Secrets',
                                                'The Prisoner of Azkaban',
                                                'The Goblet of Fire',
                                                'The Order of the Phoenix',
                                                'The Half-Blood Prince',
                                                'The Deathly Hallows']})
library.get_book('J.K.Rowling', 'The Deathly Hallows', 17, user)
print(library.books_available)
print(library.rented_books)
print(user.books)
print(library.get_book('J.K.Rowling', 'The Deathly Hallows', 10, user))
print(library.return_book('J.K.Rowling', 'The Cursed Child', user))
library.return_book('J.K.Rowling', 'The Deathly Hallows', user)
print(library.books_available)
print(library.rented_books)
print(user.books)
