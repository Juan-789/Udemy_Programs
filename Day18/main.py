# import colorgram as c
# colours = []
# colors = c.extract('hirstimage.jpg', 41)
#
# for colour in colors:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     new_colour = (r, g, b)
#     colours.append(new_colour)
#
# print(colours)
import turtle
from turtle import *

colours = [(253, 251, 247), (253, 249, 252), (232, 251, 242), (198, 13, 32), (250, 237, 19), (39, 76, 189), (39, 217, 68), (238, 227, 5), (229, 159, 47), (28, 40, 156), (214, 75, 13), (242, 246, 252), (16, 154, 16), (198, 15, 11), (243, 34, 165), (68, 10, 30), (228, 18, 120), (60, 15, 8), (223, 141, 209), (11, 97, 62), (221, 161, 9), (50, 212, 231), (18, 20, 47), (11, 227, 239), (238, 156, 217), (84, 74, 211), (78, 210, 163), (82, 234, 200), (61, 233, 241), (5, 68, 42), (216, 90, 52), (173, 178, 231), (235, 170, 164), (8, 244, 224), (248, 9, 44), (10, 77, 114), (20, 53, 243)]

tim = Turtle()
penup()
back(300)
Screen().colormode(255)

counter = 0  #i multiple of 5 increases counter 1 which makes for loop break but continue on the next row with saved index
#hard to explain lol

for i in range(len(colours)):
    if i % 9 == 0 and i != 0:
        back(700)
        right(90)
        forward(75)
        left(90)
        #goes through all
    pendown()
    color(colours[i])
    begin_fill()
    circle(20)
    end_fill()
    penup()
    forward(75)


# fillcolor(colours[0])
# end_fill()

Screen().exitonclick()