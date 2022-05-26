from turtle import Turtle
from random import randint


class TurtleRunner(Turtle):
    def __init__(self, color='lime', position=(0, 0)):
        super().__init__()
        self.name = color
        self.color(color)
        self.penup()
        self.sety(position[0])
        self.setx(-400)
        self.shape('turtle')

    def run(self):
        self.forward(randint(10, 60))

    def x_position(self):
        return self.xcor()

    def get_name(self):
        return self.name
