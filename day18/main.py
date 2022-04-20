from turtle import Turtle,\
    Screen, color, begin_fill,\
    forward, left, pos, end_fill, done

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

color('red', 'yellow')
begin_fill()
while True:
    forward(20)
    left(20)
    if abs(pos()) < 1:
        break
end_fill()
done()

screen = Screen()

screen.exitonclick()
