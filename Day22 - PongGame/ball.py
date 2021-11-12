from turtle import Turtle, xcor
import random

class Ball(Turtle):
    def __init__(self, screen_width):
        super().__init__(shape="circle")
        self.direction = [1, 1]
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.speed = [3, 0]
        self.new_direction()
        self.xbounds = (-screen_width / 2 + 10, screen_width/2 -10)

    # Used to change the direction of the ball after a reset or upon hitting a paddle
    def new_direction(self):
        self.direction[0] *= -1
        self.speed[1] = random.randint(2, 6)
        self.update()

    # Checks for collision with one of the two player paddles
    # Collision logic is simple, could be improved
    def paddleCollision(self, paddlePos, player):
        if player == 1:
            if self.distance(paddlePos) < 100 and self.ycor() > paddlePos[1] and self.xcor() < self.xbounds[0] + 20:
                self.new_direction()
                self.speed[0] += 1
        elif player == 2:
            if self.distance(paddlePos) < 100 and self.ycor() > paddlePos[1] and self.xcor() > self.xbounds[1] - 20:
                self.new_direction()
                self.speed[0] += 1

    def reset(self):
        self.setpos(0, 0)           # Reset the ball to the center
        self.speed[0] = 3           # Reset the balls speed
        self.new_direction()        # Pick a new direction for the ball to go
        
    def update(self):
        self.setx(self.xcor() + self.speed[0] * self.direction[0])        
        self.sety(self.ycor() + self.speed[1] * self.direction[1])

    