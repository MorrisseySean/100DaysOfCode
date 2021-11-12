from turtle import Turtle, Screen, colormode
import random

def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Set up our turtle
colormode(255)
t = Turtle()
t.shape('turtle')
t.color('ForestGreen')
t.speed(0)
t.pensize(20)

# Set up the screen
screen = Screen()
screen.bgcolor('black')

# Variables
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']
headings = [0, 90, 180, 270]
steps = 100
step_length = 50

for _ in range(steps):
    t.setheading(random.choice(headings))
    #t.pencolor(random.choice(colors))
    t.pencolor(get_random_color())
    t.forward(step_length)

screen.exitonclick()
    