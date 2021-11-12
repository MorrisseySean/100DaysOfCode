from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import os

# Get the base path to this folder
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# Get the highscore 
with open(THIS_FOLDER + '\highscore.txt') as file:
    highscore = file.read()

# Set screen parameters
SCREEN_SIZE = 600
screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")


initial_snake_size = 3
game_speed = 1

scoreboard = Scoreboard(SCREEN_SIZE)
scoreboard.update(highscore)
snake = Snake(initial_snake_size)
food = Food(SCREEN_SIZE)

# Register key inputs
screen.onkeypress(fun=snake.north, key="w")
screen.onkeypress(fun=snake.south, key="s")
screen.onkeypress(fun=snake.east, key="d")
screen.onkeypress(fun=snake.west, key="a")
screen.listen()

while snake.alive:
    time.sleep(game_speed / (scoreboard.score + 1))
    # Move the snake and update the screen before checking for any collisions    
    snake.update(SCREEN_SIZE)
    screen.update()
    # Check for collision with the food
    if snake.CheckCollision(food.pos()):
        snake.eat() # Increase snake size by 1
        food.move() # Move the food to a new location
        scoreboard.update(highscore) # Update the score

# When game is finished, write Game Over on the screen        
scoreboard.gameover() 
# Write the new highscore
if scoreboard.score > int(highscore):
    with open(THIS_FOLDER + '\highscore.txt', mode='w') as file:
        file.write(str(scoreboard.score))
screen.update()

screen.exitonclick()