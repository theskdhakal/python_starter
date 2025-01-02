from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.ht()
        self.score=0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score  }", align="center", font=('Arial', 12, 'normal'))

    def increase_score(self):
        self.score +=1
        self.update_score()


