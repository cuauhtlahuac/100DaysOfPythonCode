def turn_right():
    for turn in range(0,3):
        turn_left()

def jump():
    steps = 0
    while not is_facing_north():
        turn_left()
    while wall_on_right():
        move()
        steps += 1    
    turn_right()
    move()
    turn_right()
    for step in range(0, steps):
        move()
    turn_left()
        
while not at_goal():
    if not wall_in_front():
        move()
    else:
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
