from turtle import *
from random import *


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('green')
        self.speed('fastest')
        self.random_x = randint(-280, 280)
        self.random_y = randint(-280, 280)
        self.goto(self.random_x, self.random_y)
        self.refresh()

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
