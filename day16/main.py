from turtle import Turtle, Screen

# let's create a new instance of turtle
timmy = Turtle()
timmy.shape('turtle')
run_timmy = True
while run_timmy:
    timmy.right(45)

screen = Screen()

print(screen.canvheight)


def set_run_timmy():
    False


screen.onscreenclick()
screen.exitonclick()
