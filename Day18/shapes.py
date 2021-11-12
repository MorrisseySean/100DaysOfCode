from turtle import Turtle, Screen
import random

# Draw a shape of a given color, with a given number of sides.
def draw_shape(num_sides, color):
    t.pencolor(color)
    for _ in range(num_sides):
        t.forward(length)
        t.left(360/sides) 

# Set up our turtle
t = Turtle()
t.shape('turtle')
t.color('ForestGreen')
t.speed(0)

# Set up the screen
screen = Screen()
screen.bgcolor('black')

# Variables for drawing shapes
length = 100
max_sides = 10
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

for sides in range(3, max_sides):
    draw_shape(sides, random.choice(colors))

screen.exitonclick()