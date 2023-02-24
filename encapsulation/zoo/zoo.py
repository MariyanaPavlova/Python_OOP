class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity

        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget < price:
            return "Not enough budget"
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        self.__budget -= price
        self.animals.append(animal)
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return f"Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = 0
        for w in self.workers:
            needed_money += w.salary
        if needed_money > self.__budget:
            return f"You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_money
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        needed_money = 0
        for an in self.animals:
            needed_money += an.money_for_care
        if needed_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_money
        return f'You tended all the animals. They are happy. Budget left: {self.__budget}'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        result += self.__ent_str(self.animals, 'Lion')
        result += self.__ent_str(self.animals, 'Tiger')
        result += self.__ent_str(self.animals, 'Cheetah')
        return result.strip()

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        result += self.__ent_str(self.workers, 'Keeper')
        result += self.__ent_str(self.workers, 'Caretaker')
        result += self.__ent_str(self.workers, 'Vet')
        return result.strip()

    def __ent_str(self, entity, ent_tipe):
        masive = []
        for an in entity:
            if an.__class__.__name__ == ent_tipe:
                masive.append(an)
        result = f'----- {len(masive)} {ent_tipe}s:\n'
        for obj in masive:
            result += repr(obj) + '\n'
        return result


