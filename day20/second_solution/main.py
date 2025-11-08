from turtle import Screen
from Snake import Snake
import time

screen = Screen()
canvas = screen.getcanvas()

screen.setup(width=600, height=600) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

#                      x  y    x   y     x   y        
starting_positions = [(0, 0),(-20, 0) ,(-40, 0)]

segments = []

for position in starting_positions:
    segment = Snake()
    segment.goto(position)
    segment.set_name(f"name: {position[0]}")
    segment.listen_on()
    segments.append(segment)

game_is_on = True

while game_is_on:
    print("----- - Game is running - -----")
    screen.update()
    time.sleep(1)
    # segments[0].forward(20)
    for seg in segments:
        print(f"Segment {seg.name} id: {id(segment)}")
        print(f"X: {seg.xcor()} Y: {seg.ycor()}")
        # seg.print_name()
        seg.goto(segments[0].xcor(), segments[0].ycor())
        # segments[0].forward(20)
        seg.forward(20)












screen.mainloop()
screen.exitonclick()


