from turtle import Turtle, Screen



screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")


x=0
y=0
for _ in range(3):
    new_turtle=Turtle("square")
    new_turtle.color("white")
    new_turtle.goto(x,y)
    x-=20
















screen.exitonclick()