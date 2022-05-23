from turtle import Turtle


class Referee(Turtle):
    """
    Referee is a Turtle
    """
    def __init__(self, screen_width=0, screen_height=0):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.initial_point = (screen_width, screen_height)

    def draw_square(self):
        turn = 270
        for side in range(0, 4):
            self.setheading(turn)
            if side % 2 == 0:
                self.forward(self.screen_height * 2)
            else:
                self.forward(self.screen_width * 2)
            turn -= 90

    def draw_field(self):
        self.penup()
        self.goto(self.initial_point)
        self.pendown()
        self.width(3)
        self.color('green')
        self.draw_square()
        self.hideturtle()

    def get_meta(self):
        return self.screen_width

    def set_winner(self, turtle_position):
        return turtle_position >= self.screen_width

