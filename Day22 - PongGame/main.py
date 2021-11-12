import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# Detects the wall collision with the outside boundaries of the game
# and updates the games state as required.
def wallCollision(ball, scoreboard):
    # Variables for the bounds of the wall
    xbounds = (-SCREEN_WIDTH / 2 + 10, SCREEN_WIDTH/2 -10)
    ybounds = (-SCREEN_HEIGHT / 2 + 10, SCREEN_HEIGHT / 2 - 10)
    # If the ball hits the top or bottom bounds, change the y direction
    if ball.ycor() < ybounds[0] or ball.ycor() > ybounds[1]:
        ball.direction[1] *= -1
    # Check if the ball has hit the right side of the screen
    if ball.xcor() > xbounds[1]:
        ball.reset()
        scoreboard.update_score(1) # Increase player one's score and redraw the scoreboard
    # Check for a player 2 score
    if ball.xcor() < xbounds[0]:
        ball.reset()
        scoreboard.update_score(2) # Increase player two's score and redraw the scoreboard

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0) # Ensure screen doesn't update until requested

# Create two player objects and a ball object
player_one = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, 1)
player_two = Paddle(SCREEN_WIDTH, SCREEN_HEIGHT, 2)
ball = Ball(SCREEN_WIDTH)

# Scoreboard is used to manage the score of the game
scoreboard = Scoreboard(SCREEN_HEIGHT)

# Keep the game running.
game_loop = True

# This turtle is used to draw the dotted line in the center of the game screen
screen_map = Turtle(visible=False)
screen_map.sety(-SCREEN_HEIGHT / 2)
screen_map.setheading(90)
screen_map.pensize(5)
screen_map.pencolor('white')

# Draw middle line
while(screen_map.ycor() < SCREEN_HEIGHT):
    screen_map.forward(20)
    screen_map.penup()
    screen_map.forward(20)
    screen_map.pendown()

# Register player input
screen.onkeypress(fun=player_one.move_up, key='w')
screen.onkeypress(fun=player_one.move_down, key='s')
screen.onkeypress(fun=player_two.move_up, key='Up')
screen.onkeypress(fun=player_two.move_down, key='Down')
screen.listen()

while game_loop:
    # Update the players position based on player input    
    player_one.update()
    player_two.update()

    # Move the ball
    ball.update()

    # Check if the ball has collided with a paddle
    ball.paddleCollision(player_one.pos(), 1)
    ball.paddleCollision(player_two.pos(), 2)

    # Check the balls collision with the walls
    wallCollision(ball, scoreboard)
    # End the game when a player reaches 10 points
    if scoreboard.score[0] >= 10 or scoreboard.score[1] >= 10:
        game_loop = False

    # Update the screen and wait 1/60th of a second
    screen.update()
    time.sleep(1/60)


screen.exitonclick()