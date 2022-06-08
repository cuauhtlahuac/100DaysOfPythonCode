from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super(Snake, self).__init__()
        self.snake_large = 1
        self.color('white')
        self.penup()
        self.speed(6)  # o to 10
        self.shape("square")
        self.shapesize(1, self.snake_large)

    def snake_grow(self):
        self.snake_large += 1
        self.shapesize(1, self.snake_large)
