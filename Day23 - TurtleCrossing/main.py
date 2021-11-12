import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car_manager = CarManager(screen.window_height())
scoreboard = Scoreboard()

# Listen for user input to move the player.
screen.onkeypress(fun=player.move, key = 'w')
screen.listen()

game_is_on = True

while game_is_on:
    car_manager.update(player.level)
    if car_manager.collision_check(player):
        game_is_on = False
    scoreboard.draw(player.level)
    time.sleep(0.1)
    screen.update()

screen.exitonclick()