
import another_module
print(another_module.another_variable)

# in above case, we have tapped inside a variable called another_variable located in another_module


#  in the case below, we have tapped inside the Turtle class( class has capital case) inside the turtle module

# import turtle
#
# timmy=turtle.Turtle()

#  insted of above, we can import Turtle class from turtle module and just call it

from turtle import Turtle, Screen

timmy=Turtle()
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
# timmy is a new object


# ____________________________________object attribute___________________________________
my_screen=Screen()
print(my_screen.canvheight)
#  my_screen here is object and canvaheight i s the attribute

# _____________________________________object method__________________________________________
my_screen.exitonclick()