from turtle import Turtle, Screen
import prettytable
# let's create a new instance of turtle
timmy = Turtle()
timmy.shape('turtle')
run_timmy = True

screen = Screen()

print(screen.canvheight)


def set_run_timmy(coord1, coord2): # must pass the two arguments even if you don't use them
    global run_timmy # must put this in order to change the outside variable
    run_timmy = False


screen.onclick(set_run_timmy)
# screen.exitonclick()

while run_timmy:
    timmy.right(45)


