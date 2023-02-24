class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iter = 0

    def __iter__(self):
        return self

    def __next__(self):

       if self.count == self.iter:
          raise StopIteration

       cur_num = self.iter * self.step
       self.iter += 1
       return cur_num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
