from project.booths.booth import Booth
from project.delicacies.delicacy import Delicacy


class PrivateBooth(Booth):
    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)


    def reserve(self, number_of_people: int):
        price_reserv = number_of_people * Delicacy.price
        if price_reserv >=2.50:
            self.price_for_reservation = 3,50
            self.is_reserved = True