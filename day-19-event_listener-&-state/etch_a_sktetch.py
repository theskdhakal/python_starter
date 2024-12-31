from turtle import Turtle,Screen


dee=Turtle()
screen=Screen()

def move_forward():
    dee.fd(5)

def move_backward():
    dee.bk(5)

def move_clockwise():
    dee.right(5)

def move_anticlockwise():
    dee.left(5)

def clear():
    dee.reset()


screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backward)
screen.onkey(key='a',fun=move_clockwise)
screen.onkey(key='d',fun=move_anticlockwise)
screen.onkey(key='c',fun=clear)

















screen.exitonclick()