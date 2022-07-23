from prettytable import PrettyTable

pokeTable = PrettyTable()

pokeTable.add_column("Pokemon", ["Bulbasaur", "Charmander", "Sqiurtle", "Charizard"])
pokeTable.add_column("Type", ["Grass, Poison", "Fire", "Water", "Fire, Flying"])
pokeTable.align = "l"
pokeTable.add_row(["Pikachu", "Electric"])
print(pokeTable)


