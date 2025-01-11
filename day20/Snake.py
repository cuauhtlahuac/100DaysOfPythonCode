from turtle import Turtle, Screen, listen, onkeypress
from Body import Body
import time

right_heading_angle = 0
up_heading_angle = 90
left_heading_angle = 180
down_heading_angle = 270

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.speed(0)
        self.current_speed = 0.25
        #self.penup()
        
    def increase_speed(self):
        self.current_speed += 1
        
    def print_position(self):
        self.position()
        print(f"X: {self.xcor()} Y: {self.ycor()}")
        
    def turn_right(self):
        if self.heading() == right_heading_angle:
            return
        self.undo()
        self.setheading(right_heading_angle)
    
    def turn_left(self):
        if self.heading() == left_heading_angle:
            return
        self.undo()
        self.setheading(left_heading_angle)
    
    def turn_up(self):
        if self.heading() == up_heading_angle:
            return        
        self.undo()
        self.setheading(up_heading_angle)
        
    def turn_down(self):
        if self.heading() == down_heading_angle:
            return
        self.undo()
        self.setheading(down_heading_angle)
        
    def move(self):
        self.forward(20)
        time.sleep(self.current_speed)
        
    def listen_on(self):
        listen()
        onkeypress(self.turn_left, "Left")
        onkeypress(self.turn_right, "Right")
        onkeypress(self.turn_up, "Up")
        onkeypress(self.turn_down, "Down")

        

    
        