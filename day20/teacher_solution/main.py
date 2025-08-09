from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# tree squares

starting_positions = [(0,0),(-20,0), (-40,0)]
segments = []

for position in starting_positions:
    snake = Turtle()
    snake.shape("square")
    snake.color("white")
    snake.goto(position)
    segments.append(snake)

game_is_on = True

while game_is_on:
     for seg in segments:
        seg.forward(20)



















screen.exitonclick()