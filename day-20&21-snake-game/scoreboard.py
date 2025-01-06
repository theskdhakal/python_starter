from turtle import Turtle

ALIGNMENT="center"
FONT=('Arial', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.ht()
        self.highscore=0
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score  } high score:{self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_score()




