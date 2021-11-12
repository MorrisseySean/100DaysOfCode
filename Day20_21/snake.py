from turtle import Turtle

class BodyPart(Turtle):
    def __init__(self, pos):
        super().__init__(shape='square')
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.setpos(pos)

class Snake:
    def __init__(self, snake_size):
        self.body = []
        self.direction = 0
        self.speed = 20        
        self.alive = True
        self.crashed = False
        for x in range(snake_size):
            t = BodyPart((-20 * x, 0))            
            self.body.append(t)

    def move(self):
        prevPos = [0, 0]
        nextPos = self.body[0].pos()
        self.body[0].setheading(self.direction)
        self.body[0].forward(self.speed)
        for x in range(1, len(self.body)):
            prevPos = self.body[x].pos()
            self.body[x].goto(nextPos)
            nextPos = prevPos

    def CheckWallCollision(self, screen_size):
        bounds = screen_size / 2
        pos = self.body[0].pos()
        if pos[0] > bounds or pos[0] < -bounds or pos[1] > bounds or pos[1] < -bounds:
            self.alive = False

    def CheckSelfCollision(self):
        for x in range(1, len(self.body) - 1):
            if self.CheckCollision(self.body[x].pos()):
                self.alive = False
                return
    
    def CheckCollision(self, pos):
        if self.body[0].distance(pos) < 18:
            return True
        return False
    
    def eat(self):
        t = BodyPart((self.body[len(self.body) - 1].pos()))
        self.body.append(t)

    def north(self):
        if self.direction != 270:
            self.direction = 90
    
    def south(self):
        if self.direction != 90:
            self.direction = 270

    def west(self): 
        if self.direction != 0:
            self.direction = 180

    def east(self):
        if self.direction != 180:
            self.direction = 0
    
    def update(self, screen_size):
        self.move()
        self.CheckSelfCollision()
        self.CheckWallCollision(screen_size)