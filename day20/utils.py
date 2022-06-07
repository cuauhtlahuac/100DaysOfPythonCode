class KeyListener:
    def __init__(self, snake, screen):
        self.snake = snake
        self.screen = screen

    def __move_forwards__(self):
        self.snake.setheading(90)

    def __move_backwards__(self):
        self.snake.setheading(270)

    def __turn_left__(self):
        self.snake.setheading(180)

    def __turn_right__(self):
        self.snake.setheading(0)

    def keys_activate(self):
        self.screen.onkey(self.__move_forwards__, "Up")
        self.screen.onkey(self.__move_backwards__, "Down")
        self.screen.onkey(self.__turn_left__, "Left")
        self.screen.onkey(self.__turn_right__, "Right")

    def keys_unactivated(self):
        self.screen.onkey(None, "Up")
        self.screen.onkey(None, "Down")
        self.screen.onkey(None, "Left")
        self.screen.onkey(None, "Right")
