from turtle import Turtle





class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)



    def move_up(self):
        self.goto(self.xcor(),self.ycor() + 30)

    def move_down(self):
        self.goto(self.xcor(),self.ycor() - 30)
