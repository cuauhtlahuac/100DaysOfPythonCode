from turtle import Screen
from referee import Referee
from turtleRunner import TurtleRunner


def turtles_run(runners, current_referee):
    """
    :type runners: tuple of Turtles
    :type current_referee: referee
    """
    for runner in runners:
        runner.run()
        have_winner = current_referee.set_winner(runner.x_position())
        if have_winner:
            print('Winner')


screen = Screen()
screen_size = screen.screensize()
screen_width = screen_size[0]
screen_height = screen_size[1]

referee = Referee(screen_width=screen_width, screen_height=screen_height)
referee.draw_field()


tim_red = TurtleRunner('black', (0, 0))
tom_yellow = TurtleRunner('yellow', (-20, 0))
tam_orange = TurtleRunner('orange', (-40, 0))
tem_green = TurtleRunner('green', (-60, 0))
tum_blue = TurtleRunner('lime', (-80, 0))
bro_brown = TurtleRunner('brown', (-100, 0))

runners_list = (tim_red, tom_yellow, tam_orange, tem_green, tum_blue, bro_brown)

winner = False

while not winner:
    turtles_run(runners_list, referee)


screen.exitonclick()



