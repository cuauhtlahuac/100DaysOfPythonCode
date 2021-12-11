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
    
step()
step()
step()
step()
step()
step()

