class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.count:
            raise StopIteration

        res = self.count - self.i
        self.i += 1
        return res


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")