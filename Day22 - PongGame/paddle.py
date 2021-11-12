from turtle import Turtle, register_shape

class Paddle(Turtle):
    def __init__(self, screen_width, screen_height, player):
        # Setup the inital turtle paddle shape and correct the heading
        self.paddlesize = (10,100)
        register_shape('paddle', ((0, 0), (0, self.paddlesize[1]), (self.paddlesize[0], self.paddlesize[1]) ,(self.paddlesize[0], 0)))
        super().__init__(shape='paddle')
        self.color('white')
        self.speed('fastest')
        self.setheading(90)
        self.penup()    # This turtle will not be used for drawing.

        # Set the position of the paddle based on the player number
        if player == 1:
            xpos = -screen_width / 2 + self.paddlesize[0]
        else:
            xpos = screen_width / 2 - self.paddlesize[0] * 3
        self.setpos(xpos, 0)

        # Movement variables
        self.velocity = 0
        self.maxVelocity = 20
        self.acceleration = 10

        # Bound the paddle to the screen
        upperBound = screen_height / 2 - self.paddlesize[1]
        lowerBound = -screen_height / 2
        self.bounds = (upperBound, lowerBound)

    def move_up(self):
        if self.velocity < self.maxVelocity:
            self.velocity += self.acceleration

    def move_down(self):
        if self.velocity > -self.maxVelocity:
            self.velocity -= self.acceleration
    
    def update(self):
        self.forward(self.velocity)
        # Give the paddle some drift, numbers need a lot of tweaking
        if self.velocity > 0:
            self.velocity -= self.acceleration * 0.5
            if self.ycor() > self.bounds[0]:
                self.backward(self.velocity)
                self.velocity *= -1
        elif self.velocity < 0:
            self.velocity += self.acceleration * 0.5
            if self.ycor() < self.bounds[1]:
                self.backward(self.velocity)
                self.velocity *= -1
        