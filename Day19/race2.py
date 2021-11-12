import turtle
import random

colors = ['orange', 'red', 'blue', 'green']
eagle = turtle.Turtle(shape="turtle")
eagle.color(colors[0])
dragon = turtle.Turtle(shape="turtle")
dragon.color(colors[1])
lion = turtle.Turtle(shape="turtle")
lion.color(colors[2])
phoenix = turtle.Turtle(shape="turtle")
phoenix.color(colors[3])

eagle.penup()
dragon.penup()
lion.penup()
phoenix.penup()

eagle.goto(-320, -75)
dragon.goto(-320, -25)
lion.goto(-320, 25)
phoenix.goto(-320, 75)

turtle_list = [eagle, dragon, lion, phoenix]
winner = ""

while winner == "":
    for t in turtle_list:
        speed = random.randint(1, 20)
        t.forward(5)
        if t.xcor() > 320:
            winner = t

turtle.done()

