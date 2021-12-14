def turn_rigth():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_rigth()
    move()
    turn_rigth()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()