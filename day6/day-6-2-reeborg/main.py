def turn_rigth():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_rigth()
    move()
    turn_rigth()
    move()
    turn_left()

while not at_goal():
    jump()
