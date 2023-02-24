class StudentTaxes:
    def __init__(self, name, semester_tax, avr_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.avr_grade = avr_grade

    def get_discount(self):
        if self.avr_grade > 5:
            return self.semester_tax * 0.4
        # elif self.avr_grade > 4:              # Не добавяме функционалност
        #     return self.semester_tax * 0.2    # Правим нов Клас


class AddDiscount(StudentTaxes):
    def get_discount(self):
        super().get_discount()      #
        if 4 < self.avr_grade <= 5:
            return self.semester_tax * 0.2


discount = StudentTaxes('Test', 200, 5)
print(discount.get_discount())          #None

discount2 = AddDiscount('Test', 200, 5)
print(discount2.get_discount())         #40.0