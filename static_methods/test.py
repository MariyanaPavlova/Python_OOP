class Laptop:
    def __init__(self, model, memory):
        self.model = model
        self.memory = memory

    @classmethod
    def law_ram(cls, model):
        return cls(8, model)

lap = Laptop(16, 'Asus')
print(lap.model)
print(lap.memory)