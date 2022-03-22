import another_module
from turtle import Turtle, Screen

print(another_module.another_variable)

# let's create a new instance of turtle
timmy = Turtle()
timmy.shape('turtle')

timmy.right(45)

screen = Screen()

print(screen.canvheight)

screen.exitonclick()
