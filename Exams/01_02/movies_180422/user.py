from movies_180422.movie_specification.movie import Movie


class User:
    def __init__(self, username:str, age:int):
        self.age = age
        self.username = username
        self.movies_liked = []  #obj movies
        self.movies_owned = []  #obj movies

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        string = ""
        string += f"Username: {self.username}, Age: {self.age}" + "\n"
        if self.movies_liked:
            string += f"Liked movies:" + "\n"
            for i in self.movies_liked:
                string += f"{i.details()}"
        else:
            string += f"No movies liked."

        if self.movies_owned:
            string += "Owned movies:" + "\n"
            for i in self.movies_owned:
                string += f"{i.details()}"
        else:
            string += "No movies owned."
        return string