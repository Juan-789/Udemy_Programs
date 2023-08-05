from turtle import *

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def clockwise():
    tim.right(15)


def counter_clockwise():
    tim.left(15)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(counter_clockwise, "a")
screen.onkey(clear_screen, 'c')
Screen().exitonclick()
