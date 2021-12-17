# You need to run this on a web page, instruction on the README doc

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

def step():
    move()
    jump()

for step in range(0, 6):
    step()
