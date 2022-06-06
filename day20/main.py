from turtle import Turtle, Screen
from food import Food


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


def move_forwards():
    snake.setheading(90)


def move_backwards():
    snake.setheading(270)


def turn_left():
    snake.setheading(180)


def turn_right():
    snake.setheading(0)


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

game_over = False

while not game_over:
    snake.forward(4)
    food.check_is_ate(snake)

    if snake.xcor() >= screen_R_limit\
       or snake.xcor() <= screen_L_limit\
       or snake.ycor() >= screen_T_limit\
       or snake.ycor() <= screen_B_limit:
        game_over = True


screen.exitonclick()
