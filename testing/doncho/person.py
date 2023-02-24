class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    def get_info(self):
        return f'My name is {self.fullname} and I am {self.age}-years-old'
