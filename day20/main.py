from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
snake = Turtle()
snake.color('white')

snake.shape("square")

snake.shapesize(0.5, 1)


screen.exitonclick()