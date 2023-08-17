from turtle import *


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
WEST = 180
EAST = 0


class Snake:

    def __init__(self):
        self.parts = []
        self.create_snake()
        self.head = self.parts[0]

    def create_snake(self):
        for box_position in STARTING_POSITIONS:
            self.add_segment(box_position)

    def add_segment(self, box_position):
        """
        creates a new box
        :param box_position: get the item of the STARTING cords for the boxes
        and then
        :return: void
        """
        new = Turtle('square')
        new.color('White')
        new.penup()
        new.goto(box_position)
        self.parts.append(new)

    def extend(self):
        """
        add segment to snake
        :return:
        """
        self.add_segment(self.parts[-1].position())

    def move(self):
        """
        moves snake parts
        :return:
        """
        for segment in range(len(self.parts) - 1, 0, -1):
            new_x = self.parts[segment - 1].xcor()
            new_y = self.parts[segment - 1].ycor()
            self.parts[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        ***key listeners
        """
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def east(self):
        if self.head.heading() != WEST:
            self.head.seth(EAST)

    def west(self):
        if self.head.heading() != EAST:
            self.head.seth(WEST)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
