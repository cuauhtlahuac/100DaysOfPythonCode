from turtle import Turtle
from Body import Body

class Snake():
    def __init__(self):
        self.body = Body(0)
      
    def forward(self, num):
        self.body.forward(num)

    def key_up(self):
        self.body.setheading(90)
    def key_right(self):
        self.body.setheading(360)
    def key_down(self):
        self.body.setheading(270)
    def key_left(self):
        self.body.setheading(180)

    def getPosX(self):
        pos = self.body.pos()
        print("X", pos[0])
        return pos[0]
    def getPosY(self):
        pos = self.body.pos()
        return pos[1]
