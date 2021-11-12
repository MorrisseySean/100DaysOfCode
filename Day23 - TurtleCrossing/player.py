from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__(shape='turtle')# Initialise the player as a turtle shape
        self.penup()                    # We don't want this turtle to draw anything
        self.setpos(STARTING_POSITION)  # Place the turtle at the starting position
        self.setheading(90)             # Set the turtle to cross the road
        self.color('green')  
        self.level = 1           

    def move(self):
        # Move forward
        self.forward(MOVE_DISTANCE)
        # Return to the start if you get to a side of the screen.
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.level += 1
            
    pass
