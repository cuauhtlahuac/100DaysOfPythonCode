from turtle import Screen
from Snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game .")

starting_positions = [(0, 0),(-20, 0) ,(-40, 0)]

for position in starting_positions:
    segment = Snake()
    segment.goto(position)
    segment.forward(20)














screen.exitonclick()


