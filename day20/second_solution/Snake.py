from turtle import Turtle, onkeypress

right_heading_angle = 0
up_heading_angle = 90
left_heading_angle = 180
down_heading_angle = 270

class Snake(Turtle):
    def __init__(self, color_value):
        super().__init__()
        self.shape("square")
        self.color(color_value)
        self.name = "unknown"
        self.distance_behind = -20
        self.penup()
    
    def set_name(self, name):
        self.name = name

    def set_distance_behind(self, distance):
        self.distance_behind = distance

    def print_name(self):
        print("python name: ", self.name)

    def set_python_position(self, x, y):
        self.setpos(x, y)

    def turn_right(self):
        self.setheading(right_heading_angle)

    def turn_left(self):
        self.setheading(left_heading_angle)
    
    def turn_up(self):
        self.setheading(up_heading_angle)
        
    def turn_down(self):
        self.setheading(down_heading_angle)


