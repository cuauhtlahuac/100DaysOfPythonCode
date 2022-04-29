from turtle import Turtle, Screen
from css_colors import CSS_COLOR_NAMES
from random import choice

screen = Screen()
screen.bgcolor('#333')


def choice_color():
    return choice(CSS_COLOR_NAMES)


tim = Turtle()
tim.shape("turtle")
tim.color(choice_color(), choice_color())
height = screen.window_height()
tim.penup()
tim.sety((height -50) / 2)
tim.pendown()

stroke: int = 1


def draw_shape(sides):
    global stroke
    angle = 360 / sides
    for _ in range(sides):
        tim.color(choice_color())
        stroke += 0.1
        tim.width(stroke)
        tim.forward(100)
        tim.right(angle)


for number in range(3, 10):
    draw_shape(number)

screen.exitonclick()
