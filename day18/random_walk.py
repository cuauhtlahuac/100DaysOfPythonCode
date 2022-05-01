from turtle import Turtle, Screen
from css_colors import CSS_COLOR_NAMES
from random import choice, randint

screen = Screen()
screen.bgcolor('#555')
screen.setup(1000, 1000)
middle_width = screen.window_width() / 2
middle_height = screen.window_height() / 2
right_limit = middle_width
left_limit = middle_width * -1
top_limit = middle_height
bottom_limit = middle_height * -1

print(right_limit)
print(bottom_limit)

angles = [90, 0]

height = screen.window_height()
width = screen.window_width()


def choice_color():
    return choice(CSS_COLOR_NAMES)


def choice_side():
    turn = ["right", "left"]
    if choice(turn) == turn[0]:
        return tim.right
    else:
        return tim.left


def draw(distance=10):
    angle = choice(angles)
    choice_side()(angle)
    tim.color(choice_color())
    x_pos = tim.pos()[0]
    y_pos = tim.pos()[1]

    if x_pos <= left_limit:
        tim.setx(0)

    if x_pos >= right_limit:
        tim.setx(0)

    if y_pos >= top_limit:
        tim.sety(0)

    if y_pos <= bottom_limit:
        tim.sety(0)

    tim.forward(distance)


tim = Turtle()
tim.shape("classic")
tim.color(choice_color(), choice_color())
tim.width(0.1)

stroke: int = 1

while True:
    draw(25)
