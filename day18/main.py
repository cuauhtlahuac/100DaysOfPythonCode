from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color('red', 'turquoise')

timmy_the_turtle.begin_fill()

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)


while True:
    timmy_the_turtle.forward(20)
    timmy_the_turtle.left(20)
    if abs(timmy_the_turtle.pos()) < 1:
        break
timmy_the_turtle.end_fill()

screen = Screen()

screen.exitonclick()
