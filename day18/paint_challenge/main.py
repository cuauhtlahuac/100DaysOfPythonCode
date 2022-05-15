from turtle import Turtle, Screen, colormode
from random import choice
from colorgram import extract

screen_height = 1080
screen_width = 1920
dot_size = 10
padding = 20


def screen_size(distance):
    return int(distance / 2) - padding


def set_start_point(width, height):
    fix_width = screen_size(width) * -1
    fix_height = screen_size(height) * -1
    return fix_width, fix_height


colors = extract('damienHirst-Points.jpeg', 30)

screen = Screen()
screen.setup(screen_width, screen_height)
doty = Turtle()
doty.penup()
doty.goto(set_start_point(screen_width, screen_height))
doty.pendown()
doty.shape("circle")
doty.shapesize(dot_size / dot_size, dot_size / (dot_size + 1))
doty.width(dot_size)
colormode(255)
screen.tracer(2)


def color_selector():
    color = choice(colors)
    return color.rgb


def draw_dot():
    doty.color(color_selector())
    doty.penup()
    doty.dot(dot_size)


def go_left():
    doty.left(90)
    draw_dot()
    doty.forward(padding)
    draw_dot()
    doty.left(90)
    doty.forward(padding)


def go_right():
    doty.right(90)
    draw_dot()
    doty.forward(padding)
    draw_dot()
    doty.right(90)
    doty.forward(padding)


done = False
start = True
while not done:
    position = doty.pos()
    x_pos = int(position[0])
    y_pos = int(position[1])

    if y_pos >= screen_size(screen_height) and x_pos >= screen_size(screen_width):
        doty.ht()
        draw_dot()
        done = True
    else:
        if x_pos >= screen_size(screen_width):
            go_left()
        elif not start and x_pos <= (-1 * screen_size(screen_width)):
            go_right()
        else:
            draw_dot()
            doty.forward(padding)
            start = False

screen.exitonclick()
