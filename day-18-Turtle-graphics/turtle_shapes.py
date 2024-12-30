import random
from turtle import Turtle as t ,Screen
import random

timmy=t()
screen=Screen()


# for _ in range(3):
#     timmy.fd(100)
#     timmy.right(120)
#
# for _ in range(4):
#     timmy.fd(100)
#     timmy.color("red")
#     timmy.right(90)
#
# for _ in range(5):
#     timmy.fd(100)
#     timmy.color("blue")
#     timmy.right(72)


n=3
i=0
while n<11:

    vivid=["red","blue","black","green","yellow","purple","silver","skyblue"]
    angle=360/n
    chosen_color=vivid[i]


    for _ in range(n):
        timmy.fd(100)
        timmy.color(chosen_color)
        timmy.right(angle)

    n +=1
    i +=1








screen.exitonclick()