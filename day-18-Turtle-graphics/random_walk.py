import turtle as t
import random

timmy=t.Turtle()
t.colormode(255)

timmy.shape("turtle")


# saving random r, g, b color as tuple and returning which is then used to randomize color
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color_tuple=(r,g,b)
    return color_tuple



directions=[0,90,180,270]


timmy.speed(8)
timmy.pensize(15)




for _ in range(200):
    timmy.fd(40)
    timmy.color(random_color())
    timmy.setheading(random.choice(directions))


















screen=t.Screen()
screen.exitonclick()