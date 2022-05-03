from turtle import Turtle, Screen
from css_colors import CSS_COLOR_NAMES
from random import choice, randint

screen = Screen()
screen.bgcolor('#334')
screen.setup(1000, 1000)
middle_width = screen.window_width() / 2
middle_height = screen.window_height() / 2
right_limit = middle_width
left_limit = middle_width * -1
top_limit = middle_height
bottom_limit = middle_height * -1

angles = [0, 90, 180, 270]

height = screen.window_height()
width = screen.window_width()


def choice_color():
    return choice(CSS_COLOR_NAMES)


def draw(distance=10):
    angle = choice(angles)
    tim.color(choice_color())
    x_pos = tim.pos()[0]
    y_pos = tim.pos()[1]

    if x_pos <= left_limit:
        angle = 0

    if x_pos >= right_limit:
        angle = 180

    if y_pos >= top_limit:
        angle = 270

    if y_pos <= bottom_limit:
        angle = 90

    tim.setheading(angle)
    tim.forward(distance)


tim = Turtle()
tim.shape("turtle")
tim.color(choice_color(), choice_color())
tim.width(1)
tim.speed(10)

while True:
    draw(25)
