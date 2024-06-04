from turtle import Turtle

class Body(Turtle):
    def __init__(self, init_pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setpos(init_pos, 0)