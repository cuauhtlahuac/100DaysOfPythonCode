from turtle import Turtle

class Body(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.snake_large = 1
        self.color('white')
        self.shape("square")
        self.setpos(x, y)

class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.snake_large = 1
        self.color('white')
        self.penup()
        self.speed(6)  # o to 10
        self.shape("square")
        self.shapesize(1, self.snake_large)
        self.body = []

    def snake_grow(self):
        self.body.append(Body(self.xcor(), self.ycor()))
