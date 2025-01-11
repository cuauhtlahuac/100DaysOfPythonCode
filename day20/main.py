from Snake import Snake
from Food import Food

snake = Snake()

stop = False

snake.listen_on() 
 
while not stop:
    snake.move()
    snake.print_position()
    
#snake.mainloop()




