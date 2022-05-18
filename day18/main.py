from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color('red', 'turquoise')

tim.begin_fill()

for _ in range(4):
    tim.forward(100)
    tim.right(90)


while True:
    tim.forward(20)
    tim.left(20)
    if abs(tim.pos()) < 1:
        break
tim.end_fill()

screen = Screen()

screen.exitonclick()
