import turtle
from turtle import *
import random as ra


tim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = ra.randint(0, 255)
    g = ra.randint(0, 255)
    b = ra.randint(0, 255)
    return r, g, b


directions = [0, 90, 180, 270]

tim.speed('fastest')
for i in range(200):
    tim.color(random_color())
    tim.circle(100)
    tim.right(17)


Screen().exitonclick()
