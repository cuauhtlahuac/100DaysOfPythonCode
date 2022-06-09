from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(200, 200)
        self.showturtle()

    def check_is_ate(self, turtle):
        distance = (((self.xcor() - turtle.xcor()) ** 2) + ((self.ycor() - turtle.ycor()) ** 2)) ** 0.5
        if distance < 20:
            self.__create_new_food()
            turtle.snake_grow()

    def __create_new_food(self):
        self.penup()
        self.hideturtle()
        self.setpos(randint(-200, 200), randint(-200, 200))
        self.showturtle()
