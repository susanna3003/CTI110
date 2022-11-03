# CTI-110
# P4LAB2A - Turtle Graphics Shapes
# 11/3/2022
# Susanna Quayle

# import turtle

import turtle
turtle.shape("turtle")
turtle.color("green")

wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("This Turtle Can Draw!")
turtle.pensize(3)

# draw shapes

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
   

for i in range(3):
    turtle.forward(100)
    turtle.left(120)



turtle.exitonclick()
