from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Bulbasaur", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Grass", "Fire", "Water"])
table.align = "l"
print(table)
