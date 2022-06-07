from turtle import Turtle, Screen
from food import Food
from utils import KeyListener


def positive_limit(distance):
    return (distance / 2) - 25


def negative_limit(distance):
    return ((distance / 2) - 25) * -1


food = Food()

screen = Screen()
width = screen.window_width()
height = screen.window_height()

screen_R_limit = positive_limit(width)
screen_L_limit = negative_limit(width)
screen_T_limit = positive_limit(height)
screen_B_limit = negative_limit(height)

screen.bgcolor('black')
snake = Turtle()
snake.color('white')
snake.penup()
snake.speed(6)  # o to 10

snake.shape("square")
snake.shapesize(1, 2)

key_listener = KeyListener(snake, screen)
key_listener.keys_activate()
screen.listen()


game_over = False

while not game_over:
    snake.forward(4)
    food.check_is_ate(snake)

    if snake.xcor() >= screen_R_limit\
       or snake.xcor() <= screen_L_limit\
       or snake.ycor() >= screen_T_limit\
       or snake.ycor() <= screen_B_limit:
        key_listener.keys_unactivated()
        game_over = True


screen.exitonclick()
