from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
        self.is_pokemon = False

    def add_pokemon(self, pokemon: Pokemon):
        # for i in self.pokemons:
        #     if pokemon.name == i.name:
        #         self.is_pokemon = True
        #
        # if self.is_pokemon:
        #         self.is_pokemon = False
        #         return f"This pokemon is already caught"
        
        if any([pokemon.name == i.name for i in self.pokemons]):
            return f"This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon.name == pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"
        return result.strip()
