# file=open("my_file.txt")
# contents=file.read()
#
# print(contents)
#
# file.close()
#
# _____________read only mode____________________
with open("my_file.txt") as file:
    contents=file.read()

    print(contents)

# if there is no file,it will create one
# +++++++++++++++write mode+++++++++++++
with open("my_file.txt",mode="w") as file:
   file.write("NEW text")

# +++++++++++++++append mode+++++++++++++
with open("my_file.txt",mode="a") as file:
   file.write("appending her")

# from turtle import Turtle
#
# ALIGNMENT="center"
# FONT=('Arial', 12, 'normal')
#
# with open("data.txt") as file:
#     HIGH_SCORE=file.read()
#
# class ScoreBoard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.goto(0,280)
#         self.ht()
#         self.highscore=int(HIGH_SCORE)
#         self.score=0
#         self.update_score()
#
#     def update_score(self):
#         self.clear()
#         self.write(f"Score : {self.score  } high score:{self.highscore}", align=ALIGNMENT, font=FONT)
#
#     def increase_score(self):
#         self.score +=1
#         self.update_score()
#
#     def game_over(self):
#         self.goto(0,0)
#         self.write("GAME OVER", align=ALIGNMENT, font=FONT)
#
#     def reset(self):
#         if self.score > self.highscore:
#             with open("data.txt", mode="w") as file:
#                  file.write(str(self.score))
#         self.score=0
#         self.update_score()
#
#
#
#
