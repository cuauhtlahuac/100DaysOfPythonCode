from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
snake = Turtle()
snake.color('white')
snake.penup()
snake.speed(6)  # o to 10

snake.shape("square")
snake.shapesize(0.5, 1)


while True:
    snake.forward(1)


screen.exitonclick()
