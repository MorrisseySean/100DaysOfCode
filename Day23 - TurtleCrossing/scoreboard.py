FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard:
    
    def __init__(self):
        self.writer = Turtle(visible=False)
        self.writer.penup()
        self.writer.pencolor('white')
        self.writer.setpos(-300, -300)
        self.level = 0

    def draw(self, level):
        if self.level != level:
            self.level = level
            self.writer.clear()
            self.writer.pendown()
            self.writer.write(f"Level: {level}", font=FONT)

    pass
