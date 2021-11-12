from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, SCREEN_HEIGHT):
        super().__init__()
        self.fontsize = 16
        self.setpos(0, (SCREEN_HEIGHT / 2) - 16 * 2)
        self.pencolor('white')
        self.hideturtle()
        self.score = -1
        self.update(0)
   
    def update(self, highscore):
        self.clear()
        self.score += 1
        high = highscore
        if self.score > int(high):
            high = self.score
        self.write(f"Score: {self.score}    Highscore: {high}", False, 'center', ('Arial', self.fontsize, 'bold'))

    def gameover(self):
        self.penup()
        self.setpos(0, 0)
        self.pendown()
        self.write("Game Over", False, 'center', ('Arial', self.fontsize, 'bold'))