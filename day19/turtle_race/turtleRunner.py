from turtle import Turtle
from random import randint


class TurtleRunner(Turtle):
    def __init__(self, color='lime', position=(0, 0)):
        super().__init__()
        self.color(color)
        self.sety(position[0])
        self.setx(-400)
        self.shape('turtle')
        self.penup()

    def run(self):
        self.forward(randint(10, 70))

    def x_position(self):
        return self.xcor()
