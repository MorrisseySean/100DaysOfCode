from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, screen_height):
        # Setup the turtle
        super().__init__(visible = False)
        self.pencolor('white')
        self.penup()
        self.speed('fastest')

        # Set the variables required for drawing the score
        self.fontsize = 50
        self.space = 100
        # The inital score is set to -1 as the first update will change the score to [0,0]
        self.score = [-1, 0] 

        # Move the turtle to the correct position before drawing the initial score
        self.sety(screen_height / 2 - (self.fontsize * 2))
        self.backward(self.space / 2)
        self.update_score(1)
    
    # A function used to update the score and redraw it on the screen.
    def update_score(self, player):
        self.score[player - 1] += 1 # Update score
        self.clear()                # Clear previous score
        self.pendown()
        self.write(self.score[0], align='center', font=('Calibri', self.fontsize, 'normal'))
        self.penup()
        self.forward(self.space)    # Draw second score on the other side of the board.
        self.pendown()
        self.write(self.score[1], align='center', font=('Calibri', self.fontsize, 'normal'))
        self.penup()
        self.backward(self.space)   # Reset turtle position for next score refresh

