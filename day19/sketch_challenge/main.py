# W = Forwards
# S = Backwards
# A = Counter-clockwise
# D = Clockwise

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forwards():
    tim.forward(10)


def backwards():
    tim.backward(10)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


screen.onkey(forwards, 'w')
screen.onkey(backwards, 's')
screen.onkey(counter_clockwise, 'a')
screen.onkey(clockwise, 'd')


screen.listen()
screen.exitonclick()

