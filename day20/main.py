from turtle import Turtle, Screen
from food import Food

food = Food()

screen = Screen()
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


while True:
    snake.forward(4)
    food.check_is_ate(snake)


screen.exitonclick()
