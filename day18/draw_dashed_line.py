import turtle as t
from turtle import Screen

tim = t.Turtle()
screen = Screen()

########### Challenge 2 - Draw a Dashed Line ########
win_width = screen.window_width()
tim.shape("turtle")
tim.pencolor('red')
tim.penup()
tim.setx(-1 * (win_width / 2))
tim.width(3)
tim.pendown()

for _ in range(int(win_width / 20)):
    if abs(tim.xcor()) > win_width / 2:
        tim.right(90)

    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


screen.exitonclick()
