from prettytable import PrettyTable, MARKDOWN

table_x = PrettyTable()
table_x.set_style(MARKDOWN)
table_x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table_x.add_column("Type", ["Electric", "water", "Fire"])

print(table_x)
