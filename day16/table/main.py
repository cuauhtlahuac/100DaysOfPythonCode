from prettytable import PrettyTable, MARKDOWN

table_x = PrettyTable()
table_x.set_style(MARKDOWN)
table_x.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table_x.add_column("Type", ["Electric", "water", "Fire"])
table_x.left_padding_width = 5
table_x.right_padding_width = 5
print(table_x)
