# CTI-110
# P4LAB2B - Turtle Graphics Initials
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

# draw initials

turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.penup()
turtle.forward(20)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(100)
turtle.penup()
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(80)
turtle.left(45)
turtle.pendown()
turtle.forward(45)

turtle.exitonclick()
