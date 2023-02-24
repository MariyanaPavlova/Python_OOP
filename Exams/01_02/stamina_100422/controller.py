
from stamina_140422.player import Player
from stamina_140422.supply.drink import Drink
from stamina_140422.supply.food import Food
from stamina_140422.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []  #obj
        self.supplies = []  #obj

    def add_player(self, *players):
        added_player = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_player.append(player.name)
        return f"Successfully added: {', '.join(added_player)}"

    def add_supply(self, *supplies):
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self.__find_player_by_name(player_name)
        if player is None:
            return
        if sustenance_type != 'Food' and sustenance_type != 'Drink':
            return

        ind, find_supply = self.__find_supply_by_type(sustenance_type)
        if find_supply is None:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        if player.need_sustenance == False:
            return f"{player_name} have enough stamina."

        player.stamina = min(player.stamina + find_supply.energy, 100)

        self.supplies.pop(ind)
        return f"{player_name} sustained successfully with {find_supply.name}."


    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player_by_name(first_player_name)
        second_player = self.__find_player_by_name(second_player_name)

        error_mess = ''
        if first_player.stamina ==0:
            error_mess += f"Player {first_player.name} does not have enough stamina."
        if second_player.stamina == 0:
            error_mess += '\n' + f"Player {second_player.name} does not have enough stamina."
        if error_mess:
            return error_mess.strip()

        if second_player.stamina < first_player.stamina:
            first_player, second_player = second_player, first_player

        first_player_damage = first_player.stamina / 2
        second_player.stamina = max(second_player.stamina - first_player_damage, 0)
        if second_player.stamina == 0:
            return f'Winner: {first_player.name}'

        second_player_damage = second_player.stamina / 2
        first_player.stamina = max(first_player.stamina - second_player_damage, 0)
        if first_player.stamina == 0:
            return f'Winner: {second_player.name}'

        winner = first_player if first_player.stamina > second_player.stamina else second_player
        return f'Winner {winner.name}'


    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age *2, 0)
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')


    def __str__(self):
        result = ''
        for player in self.players:
            result += str(player)+ '\n'
        for supply in self.supplies:
            result += supply.details() +'\n'
        return result.strip()


    def __find_player_by_name(self, player_name): #помощна
        for player in self.players:
            if player.name == player_name:
                return player

    def __find_supply_by_type(self, sustenance_type): #помощна
        for ind in range(len(self.supplies )-1, -1, -1):
            supply = self.supplies[ind]
            if supply.__class__.__name__== sustenance_type:
                return (ind, supply)
        return (-1, None) #за да няма невалиден инд ако не намери supply



# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)
