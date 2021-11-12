from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.speed(0)

def move_forwards():
    t.forward(10)

def move_backwards():
    t.backward(10)

def turn_left():
    t.left(10)

def turn_right():
    t.right(10)

def clear_screen():
    t.reset()



screen.onkeypress(fun=move_forwards,key='w')
screen.onkeypress(fun=move_backwards,key='s')
screen.onkeypress(fun=turn_left,key='a')
screen.onkeypress(fun=turn_right,key='d')
screen.onkey(fun=clear_screen, key='c')

screen.listen()

screen.exitonclick()