from turtle import Turtle, listen, onkeypress

right_heading_angle = 0
up_heading_angle = 90
left_heading_angle = 180
down_heading_angle = 270

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
    
    def set_name(self, name):
        self.name = name

    def print_name(self):
        print("name", self.name)

    def turn_right(self):
        if self.heading() == right_heading_angle:
            return
        self.setheading(right_heading_angle)

    def turn_left(self):
        if self.heading() == left_heading_angle:
            return
        self.setheading(left_heading_angle)
    
    def turn_up(self):
        if self.heading() == up_heading_angle:
            return        
        self.setheading(up_heading_angle)
        
    def turn_down(self):
        if self.heading() == down_heading_angle:
            return
        self.setheading(down_heading_angle)

    def listen_on(self):
        listen()
        onkeypress(self.turn_left, "Left")
        onkeypress(self.turn_right, "Right")
        onkeypress(self.turn_up, "Up")
        onkeypress(self.turn_down, "Down")

