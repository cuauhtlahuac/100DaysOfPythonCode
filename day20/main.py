from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor('black')
snake = Turtle()
snake.color('white')
snake.penup()
snake.speed(6)  # o to 10

snake.shape("square")
snake.shapesize(1, 2)

food = Turtle()
food.shape("square")
food.shapesize(1, 1)
food.color('white')
food.penup()
food.hideturtle()
food.setpos(200, 200)
food.showturtle()


def move_forwards():
    snake.setheading(90)


def move_backwards():
    snake.setheading(270)


def turn_left():
    snake.setheading(180)


def turn_right():
    snake.setheading(0)


def create_food():
    food.color('red')


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# TODO: detect collision with food and create a random new one

while True:
    snake.forward(1)


screen.exitonclick()