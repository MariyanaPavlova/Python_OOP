from project_1508.person import Person
from project_1508.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

