from turtle import Turtle

class Body(Turtle):
    def __init__(self):
        self.next = None
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")