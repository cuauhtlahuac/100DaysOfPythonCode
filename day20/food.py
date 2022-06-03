from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        # self.shapesize(1, 1)
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setpos(200, 200)
        self.x_pos = self.xcor()
        self.start_x_pos = self.x_pos + 20
        self.end_x_pos = self.x_pos - 20
        self.showturtle()

    def check_is_ate(self, turtle):
        turtle_x_pos = turtle.xcor()
        turtle_start_x_pos = turtle_x_pos + 20
        turtle_end_x_pos = turtle_x_pos - 20

        if self.start_x_pos == turtle_start_x_pos or self.end_x_pos == turtle_start_x_pos:
            print("COLITION with start", )

        if self.start_x_pos == turtle_end_x_pos or self.end_x_pos == turtle_end_x_pos:
            print("COLITION with start", )

