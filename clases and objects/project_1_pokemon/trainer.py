from project_1_pokemon.pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            #any e същото като len(self.pokemons) > 0
        #if any([x for x in self.pokemons if x.name == pokemon.name]):
            return f'This pokemon is already caught'
        else:
            self.pokemons.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name: str):
        for pok in self.pokemons:
            if pok.name == pokemon_name:
                self.pokemons.remove(pok)
                return f"You have released {pokemon_name}"

        return f'Pokemon is not caught'

    def trainer_data(self):
        result = ""
        result += f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            result += "- " + p.pokemon_details()

        return result

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
