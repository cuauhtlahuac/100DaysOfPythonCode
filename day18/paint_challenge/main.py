from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract

colors = extract('damienHirst-Points.jpeg', 10)


def color_selector():
    color = choice(colors)
    return color.rgb


def draw_dots():
    doty.color(color_selector())
    doty.penup()
    doty.dot(20)
    doty.forward(40)
    doty.pendown()


screen = Screen()
screen.setup(400, 400)
doty = Turtle()
doty.penup()
doty.goto(-160, -160)
doty.pendown()
doty.shape("circle")
doty.width(20)
colormode(255)
#screen.tracer(25)


number = 0
while True:
    draw_dots()
    number += 1
    if number == 8:
        doty.left(90)
        number = 0
        doty.penup()
        doty.forward(40)
        doty.pendown()
        doty.left(90)




screen.exitonclick()
