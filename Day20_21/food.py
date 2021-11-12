from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, screen_size):
        super().__init__(shape='circle')
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.screen_size = screen_size - 40
        self.move()
    
    def move(self):
        yPos = random.randint(-self.screen_size / 2, self.screen_size / 2)
        xPos = random.randrange(-self.screen_size / 2, self.screen_size / 2, 20)
        yPos = random.randrange(-self.screen_size / 2, self.screen_size / 2, 20)
        self.goto(xPos, yPos)