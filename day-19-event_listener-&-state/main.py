from turtle import Turtle, Screen



timmy=Turtle()
screen=Screen()

timmy.penup()
timmy.goto(-300,-200)

def move_forward():
    timmy.pendown()
    timmy.setheading(90)
    timmy.fd(200)
    timmy.setheading(0)
    timmy.fd(100)
    timmy.setheading(180)
    timmy.fd(100)
    timmy.setheading(270)
    timmy.fd(100)
    timmy.setheading(0)
    timmy.fd(100)

    timmy.penup()
    timmy.fd(30)
    timmy.pendown()

    timmy.setheading(270)
    timmy.fd(100)
    timmy.setheading(0)
    timmy.fd(70)
    timmy.setheading(90)
    timmy.fd(100)

    timmy.setheading(0)
    timmy.penup()
    timmy.fd(130)
    timmy.pendown()

    timmy.setheading(180)
    timmy.fd(100)
    timmy.left(90)
    timmy.fd(100)
    timmy.left(90)
    timmy.fd(100)

    timmy.penup()
    timmy.fd(30)
    timmy.pendown()


    timmy.setheading(90)
    timmy.fd(200)
    timmy.setheading(270)
    timmy.fd(100)
    timmy.setheading(45)
    timmy.fd(100)
    timmy.bk(100)
    timmy.setheading(305)
    timmy.fd(100)






screen.listen()
screen.onkey(fun=move_forward,key='space')
screen.exitonclick()