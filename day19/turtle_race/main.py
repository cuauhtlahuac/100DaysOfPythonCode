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
        current_referee.set_game_over(runner)


def get_color_list_text(colors_list):
    colors_text = ''
    for index in range(0, len(colors_list)):
        color = colors_list[index]
        colors_text += f"[{index + 1}]: {color}\n"
    return colors_text


screen = Screen()
screen.title('Awesome Turtle Race')
screen.bgcolor('lime green')
screen_size = screen.screensize()
screen_width = screen_size[0]
screen_height = screen_size[1]

referee = Referee(screen_width=screen_width, screen_height=screen_height)
screen.tracer(2)
referee.draw_field()

colors = ('red', 'yellow', 'dark orange', 'dark green', 'deep pink', 'sienna')

tim_red = TurtleRunner(colors[0], (0, 0))
tom_yellow = TurtleRunner(colors[1], (-20, 0))
tam_orange = TurtleRunner(colors[2], (-40, 0))
tem_green = TurtleRunner(colors[3], (-60, 0))
tum_blue = TurtleRunner(colors[4], (-80, 0))
bro_brown = TurtleRunner(colors[5], (-100, 0))

screen.tracer(1)
runners_list = (tim_red, tom_yellow, tam_orange, tem_green, tum_blue, bro_brown)
referee.set_runners_list(runners_list)

guessing = screen.textinput('Select the number of the winner', get_color_list_text(colors))
referee.set_guessing(guessing)

while not referee.terminated:
    if referee.terminated:
        break
    else:
        turtles_run(runners_list, referee)

referee.final_positions()

screen.exitonclick()



