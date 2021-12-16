def turn_rigth():
    for step in range(0,3):
        turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if not wall_on_right():
        turn_rigth()
    if wall_in_front():
        turn_left()
  