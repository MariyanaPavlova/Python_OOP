class dictionary_iter:
    def __init__(self, data):
        self.data = list(data.items())
        self.ind = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind >= len(self.data):
            raise StopIteration()

        result = self.data[self.ind]
        self.ind += 1
        return result


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)