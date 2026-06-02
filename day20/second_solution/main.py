from turtle import Screen, listen, onkeypress
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
colors = ["red", "yellow", "blue"]

segments = []

for index, position in enumerate(starting_positions):
    segment = Snake(colors[index])
    segment.goto(position)
    segment.set_distance_behind(position[0])
    segment.set_name(f"snake_{index} ")
    segments.append(segment)

game_is_on = True

listen()

head = segments[0]

onkeypress(head.turn_left, "Left")
onkeypress(head.turn_right, "Right")
onkeypress(head.turn_up, "Up")
onkeypress(head.turn_down, "Down")

while game_is_on:
    print("----- - Game is running - -----")
    screen.update()
    time.sleep(1)
    for index, seg in enumerate(segments):
        seg.print_name()
        if id(seg) == id(head):
            print(f"is head: X: {head.xcor()} Y: {head.ycor()}")
            head.forward(20)
        else:
            print(f"X: {seg.xcor()} Y: {seg.ycor()}")
            seg.set_python_position(head.xcor() + seg.distance_behind, head.ycor() + seg.distance_behind)
            
        
    












screen.mainloop()
screen.exitonclick()


