# import colorgram
#
# colors=colorgram.extract("image.jpg",20)
#
# color_list=[]
#
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     color_list.append(new_color)
#
# print(color_list)

import turtle as t
import random

dee=t.Turtle()
dee.shape("turtle")
t.colormode(255)

screen=t.Screen()


color_list=[(228, 227, 226), (246, 237, 243), (243, 244, 246), (234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33)]


x=-250
y=-200
dee.penup()
dee.speed("fastest")
dee.goto(x,y)

for dot_count in range(1,101):
    dee.dot(20,random.choice(color_list))
    dee.penup()
    dee.fd(50)

    if dot_count % 10 ==0:
        dee.setheading(90)
        dee.forward(50)
        dee.left(90)
        dee.fd(500)
        dee.setheading(0)


dee.ht()







screen.exitonclick()