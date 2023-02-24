class Race:
    def __init__(self, name:str):
        self.name = name
        self.drivers = [] #obj drivers

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError(f"Name cannot be an empty string!")
        self.__name = value
