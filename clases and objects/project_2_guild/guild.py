from project_2_guild.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player_p):
        if player_p.guild == self.name:
            return f'Player {player_p.name} is already in the guild.'

        elif player_p.guild != self.name and player_p.guild != "Unaffiliated":
            return f"Player {player_p.name} is in another guild."

        self.players.append(player_p)
        player_p.guild = self.name
        return f'Welcome player {player_p.name} to the guild {self.name}'

    def kick_player(self, player_name):
        for pl in self.players:
            if pl.name == player_name:
                pl.guild = "Unaffiliated"
                self.players.remove(pl)
                return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f'Guild: {self.name}\n'

        for pl in self.players:
            result += f'{pl.player_info()}'
        return result

player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())

guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
