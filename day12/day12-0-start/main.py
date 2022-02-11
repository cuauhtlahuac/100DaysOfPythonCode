################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}") # print 2

increase_enemies()
print(f"enemies outside function: {enemies}") # print 1


if 3 > 2:
    a_variable = 10

print(a_variable) # it can access 