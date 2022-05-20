from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def draw_line():
    tim.forward(10)


screen.onkey(draw_line, 'space')

screen.listen()
screen.exitonclick()

