from movies_180422.movie_specification.movie import Movie
from movies_180422.movie_specification.fantasy import Fantasy
from movies_180422.movie_specification.action import Action
from movies_180422.movie_specification.thriller import Thriller
from movies_180422.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = [] #obj movies
        self.users_collection = [] #obj users

    def __find_user_in_app(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True

    def __find_users_movie(self, movie: Movie):
        for movie in self.movies_collection:
            if movie.title == movie.title:
                return True

    def __checked_if_user_liked(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False


    def register_user(self, username, age):
        if self.__find_user_in_app(username):
            raise Exception('User already exists!')

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        if not self.__find_user_in_app(username):
            return f"This user does not exist!"

        elif self.__find_user_in_app(username):
            self.movies_collection.append(movie)
            user.movies_owned.append(movie)
            return f"{username} successfully added {movie.title} movie."

        if self.__find_user_in_app(username) and self.__find_users_movie(movie):
            return "Movie already added to the collection!"
        elif username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')


    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if not self.__find_users_movie(movie):
            raise Exception('The movie {movie.title} is not uploaded!')
        elif username != movie.owner.username:
             raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        if not self.__find_users_movie(movie):
             raise Exception(f'The movie {movie.title} is not uploaded!')
        elif username != movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.pop(self.movies_collection.index(movie))

            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.pop(user.movies_owned.index(movie))
                    return f'{username} successfully deleted {movie.title} movie.'


    def like_movie(self, username: str, movie: Movie):
        if username == movie.owner.username:
             raise Exception(f'{username} is the owner of the movie {movie.title}!')
        if self.__checked_if_user_liked(username, movie):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes +=1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
            return f'{username} liked {movie.title} movie.'


    def dislike_movie(self, username: str, movie: Movie):
        if not self.__checked_if_user_liked(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -=1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
        return f'{username} disliked {movie.title} movie.'


    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'


# movie_app = MovieApp()
# print(movie_app.register_user('Martin', 24))
# user = movie_app.users_collection[0]
# movie = Action('Die Hard', 1988, user, 18)
# print(movie_app.upload_movie('Martin', movie))
# print(movie_app.movies_collection[0].title)
# print(movie_app.register_user('Alexandra', 25))
# user2 = movie_app.users_collection[1]
# movie2 = Action('Free Guy', 2021, user2, 16)
# print(movie_app.upload_movie('Alexandra', movie2))
# print(movie_app.edit_movie('Alexandra', movie2, title="Free Guy 2"))
# # print(movie_app.like_movie('Martin', movie2))
# # print(movie_app.like_movie('Alexandra', movie))
# # print(movie_app.dislike_movie('Martin', movie2))
# # print(movie_app.like_movie('Martin', movie2))
# print(movie_app.delete_movie('Alexandra', movie2))
# # movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
# # print(movie_app.upload_movie('Alexandra', movie2))
# # print(movie_app.display_movies())
# # print(movie_app)
