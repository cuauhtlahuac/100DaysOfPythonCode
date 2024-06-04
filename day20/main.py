from turtle import Screen
from Snake import Snake
from Food import Food

screen = Screen()
width = screen.window_width()
height = screen.window_height()

right_bound = (width / 2) - 20
left_bound = ((-1 * width) / 2) + 12
top_bound = (height / 2) - 14
bottom_bound = ((-1 * height) / 2) + 20

screen.bgcolor('black')

snake = Snake()
food = Food(right_bound - 100)

# move the snake (straight)

screen.onkeypress(snake.key_up , 'Up')
screen.onkeypress(snake.key_right , 'Right')
screen.onkeypress(snake.key_down, 'Down')
screen.onkeypress(snake.key_left, 'Left')
screen.listen()


play = True
def setPlay():
    global play
    play = True
    print("r pressed:", play)

screen.onkeypress(setPlay, 'r')

# Create a snake body (3 squares)


while play:
    # Control the snake
    snake.forward(2)

# Create a score board (Score: 0)
   
    x = snake.getPosX()
    y = snake.getPosY()
    print("FOOD---", food.left_limit, "Y", food.top_limit)
# Detect collision with food (when touch food, a new one appears in a random place)
    if(x == food.left_limit and y == food.top_limit):
        screen.bgcolor('pink')
        play = False
    elif(x == food.right_limit and y == food.top_limit):
        screen.bgcolor('red')
        play = False

# Detect collision with wall (Game Over.)
    if( x >= right_bound):
        screen.bgcolor('green')
        play = False
    elif( x <= left_bound ):
        screen.bgcolor('blue')
        play = False
    if( y  >= top_bound ):
        screen.bgcolor('gray')
        play = False
    elif( y <= bottom_bound ):
        screen.bgcolor('red')
        play = False
        
screen.onclick()
screen.exitonclick()


