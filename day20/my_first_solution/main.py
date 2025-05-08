from Snake import Snake
from Food import Food

snake = Snake()

stop = False

screen_x_size = 600
screen_y_size = 600

limit_x_size = 420
limit_y_size = 420

screen = snake.get_screen()
screen.setup(width=screen_x_size , height=screen_x_size, startx=100, starty=100)
screen.screensize(screen_x_size - 10, screen_y_size - 10, "green")
height = screen.window_height()
width = screen.window_width()
snake.draw_screen_limits(limit_x_size, limit_y_size)

snake.listen_on()

def game_over():
    snake.goto(0, 0)
    snake.write("Game Over", align="center", font=("Arial", 24, "normal"))
    return True

snake.create_body()
snake.new_snake()
while not stop:
    snake.move()
    snake.new_snake.move()
   # snake.print_position()
    if(
        snake.get_x_position() >= (limit_x_size - 48) / 2 
        or snake.get_x_position() <= (-limit_x_size + 48) / 2
        or snake.get_y_position() >= (limit_y_size - 48) / 2
        or snake.get_y_position() <= (-limit_y_size + 48) / 2
    ):
        stop = game_over()

screen.exitonclick()
    
#snake.mainloop()




