import turtle as t
import random

shaun=t.Turtle()
t.colormode(255)
shaun.speed("fastest")

def random_colors():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    my_color=(r,g,b)
    return my_color


def draw_spirograph(size_of_gap):
    for degree in range(int(360/size_of_gap)):
        shaun.setheading(shaun.heading()+ size_of_gap)
        shaun.color(random_colors())
        shaun.circle(50)

draw_spirograph(10)



















screen=t.Screen()
screen.exitonclick()