from project_1508.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    def make_sound(self):
        return "Hiss"