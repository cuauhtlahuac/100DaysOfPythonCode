from turtle import Turtle, Screen, colormode
from random import randint

screen = Screen()
spyro = Turtle()
spyro.shape("circle")
colormode(255)
screen.tracer(25)  # speed up


def choice_color():
    r = randint(10, 255)
    g = randint(10, 255)
    b = randint(10, 255)
    return r, g, b


def draw_circle(length):
    spyro.color(choice_color())
    spyro.circle(100)
    spyro.left(length)


def spyral():
    distance = 4
    times = 360 / distance
    spyro.begin_fill()

    for _ in range(0, int(times)):
        draw_circle(distance)

    spyro.end_fill()


spyral()

screen.exitonclick()
