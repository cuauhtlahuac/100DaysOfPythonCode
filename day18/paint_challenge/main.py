from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract

colors = extract('damienHirst-Points.jpeg', 30)

screen = Screen()
screen.setup(400, 400)
doty = Turtle()
doty.penup()
doty.goto(-160, -160)
doty.pendown()
doty.shape("circle")
doty.width(20)
colormode(255)
# screen.tracer(3)


def color_selector():
    color = choice(colors)
    return color.rgb


def draw_dot():
    doty.color(color_selector())
    doty.penup()
    doty.dot(20)


def go_left():
    doty.left(90)
    draw_dot()
    doty.forward(40)
    draw_dot()
    doty.left(90)
    doty.forward(40)


def go_right():
    doty.right(90)
    draw_dot()
    doty.forward(40)
    draw_dot()
    doty.right(90)
    doty.forward(40)


done = False
start = True
while not done:
    position = doty.pos()
    x_pos = int(position[0])
    y_pos = int(position[1])

    if y_pos >= 160 and x_pos >= 160:
        draw_dot()
        done = True
    else:
        if x_pos >= 160:
            go_left()
        elif not start and x_pos <= -160:
            go_right()
        else:
            draw_dot()
            doty.forward(40)
            start = False


screen.exitonclick()
