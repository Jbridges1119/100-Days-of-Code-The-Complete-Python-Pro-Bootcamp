from prettytable import PrettyTable
# assign class to table (doesn't need new)
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table.align)
table.align = "l"
print(table.align)
print(table)