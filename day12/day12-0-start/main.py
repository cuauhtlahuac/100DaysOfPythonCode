################### Scope ####################

enemies = 1 # this is a global scope variable

def increase_enemies():
  enemies = 2 # here it creates a new local scope variable, thats why it prints 2 instead 1
  print(f"enemies inside function: {enemies}") # print 2

def increase_enemies_global():
  global enemies # to use the variable outside fo the function (NO RECOMMENDED)
  enemies += 1
  print(f"enemies inside function: {enemies}") # print 2

increase_enemies()
print(f"enemies outside function: {enemies}") # print 1


if 3 > 2:
    a_variable = 10

print(a_variable) # it can access 