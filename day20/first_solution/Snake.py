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
        self.turtlesize(stretch_wid=1, stretch_len=1, outline=0)
        
    def increase_speed(self):
        self.current_speed += 1
        
    def print_position(self):
        self.position()
        print(f"X: {self.xcor()} Y: {self.ycor()}")
        
    def get_x_position(self):
        return self.xcor()
    
    def get_y_position(self):
        return self.ycor()

    def get_screen(self):
        return Screen()
    
    def move(self):
        self.forward(20)
        time.sleep(self.current_speed)
        print(f"X: {self.xcor()} Y: {self.ycor()}")

    def new_snake(self):
        self.new_snake = Snake()

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
        
    def listen_on(self):
        listen()
        onkeypress(self.turn_left, "Left")
        onkeypress(self.turn_right, "Right")
        onkeypress(self.turn_up, "Up")
        onkeypress(self.turn_down, "Down")
        
    # deetectar la dirección de la serpiente
    def detect_direction(self):
        return self.heading()
    # hacer nacer un nuevo cuerpo cuando colisione con el otro 
    def create_body(self):
        body = Body()
        body.setx(self.xcor())
        body.sety(self.ycor() - 20)
        body.setheading(self.heading())
        return body
        
    def draw_screen_limits(self, width, height):
        half_width = width / 2
        half_height = height / 2
        
        thick_w_line =  half_width + 5
        thick_h_line = half_height + 5
        
        #self.pencolor("white")
        #self.pensize(0)
        self.penup()
        #self.goto(-half_width, half_height)
        #self.pendown()
        #self.goto(-half_width, -half_height)
        #self.goto(half_width, -half_height)
        #self.goto(half_width, half_height)
        self.goto(-half_width, half_height)
        self.penup()
        self.pensize(9)
        self.pencolor("white")
        self.goto(-thick_w_line, thick_h_line)
        self.pendown()
        self.goto(-thick_w_line, -thick_h_line)
        self.goto(thick_w_line, -thick_h_line)
        self.goto(thick_w_line, thick_h_line)
        self.goto(-thick_w_line, thick_h_line)
        self.penup()
        self.goto(0,0)
        self.pensize(1)
        self.pencolor("white")
        self.pendown()
        

    
        