from turtle import Screen
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game .")

# tree squares

snake = Snake()
snake_2 = Snake()
snake_3 = Snake()
snake_2.goto(-20,0)
snake_3.goto(-40,0)














screen.exitonclick()


