from turtle import Turtle, Screen
import random

screen=Screen()

is_race_on=False

screen.setup(width=500,height=400)


colors=["red","blue","green","yellow","purple","orange","black"]
all_turtles=[]


x=-230
y=-150
for color_name in colors:
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color_name)
    new_turtle.goto(x,y)
    y += 50
    all_turtles.append(new_turtle)

user_bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter the color : ")


if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >220:
            is_race_on=False
            winning_color=turtle.pencolor()

            if winning_color == user_bet:
                print(f"You have won ! The {winning_color} is the winner !")
            else:
                print(f"You have won ! The {winning_color} is the winner !")


        random_distance=random.randint(0,10)
        turtle.fd(random_distance)













screen.exitonclick()