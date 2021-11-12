import colorgram
import os
from turtle import Turtle, Screen, colormode
import random

def get_color():
    return random.choice(colors).rgb

## --- Objects --- ##
screen = Screen()
t = Turtle()

# Extract colors from image and place them in a list
colormode(255)
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'hirst.jpg')
colors = colorgram.extract(my_file, 10)

# Drawing variables
dot_size = 40 
dot_space = dot_size * 2

# Find the amount of dots required to fill the screen.
screen = Screen()
drawing_size = [int(screen.window_width() / dot_space ), int(screen.window_height() / dot_space)]

# Turtle setup
t.speed('fastest') 
t.hideturtle()
t.penup() 

# Start the turtle in the bottom left of the screen.
position = t.pos()
t.setx((position[0] + dot_size) - (screen.window_width() / 2))
t.sety((position[1] + dot_size) - (screen.window_height() / 2))

for x in range(drawing_size[1]):
    position = t.pos()
    direction = t.heading()
    for y in range(drawing_size[0]): 
        t.dot(dot_size, get_color())
        t.forward(dot_space)
    t.setx(position[0])
    t.sety(position[1] + dot_space)    
    
screen.exitonclick()