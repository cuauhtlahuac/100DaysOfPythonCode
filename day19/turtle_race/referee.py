from turtle import Turtle


def get_position(turtle):
    return turtle.x_position()


class Referee(Turtle):
    """
    Referee is a Turtle too
    """

    def __init__(self, screen_width=0, screen_height=0):
        self.terminated = False
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.initial_point = (screen_width, screen_height)
        self.winner = None
        self.runners_list = None
        self.guess_number = None

    def draw_quadrilateral(self, height, width):
        turn = 270
        for side in range(0, 4):
            self.setheading(turn)
            if side % 2 == 0:
                self.forward(height)
            else:
                self.forward(width)
            turn -= 90

    def draw_field(self):
        self.penup()
        self.goto(self.initial_point)
        self.pendown()
        self.width(3)
        self.color('white')
        self.draw_quadrilateral(self.screen_height * 2, self.screen_width * 2)
        self.hideturtle()

    def get_meta(self):
        return self.screen_width

    def set_runners_list(self, runners_list):
        """
        Mandatory.
        referee needs to know the participants
        :param runners_list:
        :return: void
        """
        self.runners_list = runners_list

    def set_guessing(self, guess):
        self.guess_number = int(guess)

    def set_game_over(self, turtle):
        if turtle.x_position() + 20 >= self.screen_width:
            self.terminated = True
            return self

    def final_positions(self):
        sorted_list = sorted(self.runners_list, key=get_position, reverse=True)
        for index in range(0, len(sorted_list)):
            runner = sorted_list[index]
            style = ('Arial', 10, 'italic')
            winner_style = ('Arial', 24, 'italic')
            br = '\n'
            space = ' '
            if index == 0:
                runner.write(f"\nwinner!", font=winner_style, align='center')
            else:
                runner.write(f"{br * 3}P: {index + 1}{space * 4}", font=style, align='right')

        referee_style = ('Arial', 24, 'italic')
        self.setx(-24)
        if sorted_list[0].get_name() == self.runners_list[self.guess_number - 1].get_name():
            self.color('white')
            self.write('YOU WIN!', font=referee_style)
        else:
            self.color('red')
            self.write('YOU LOSE!', font=referee_style)
