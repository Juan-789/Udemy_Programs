from turtle import *
from random import *


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ['purple', 'orange', 'green', 'yellow', 'red', 'blue']  # make algo to automatize lol
vert = -70
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(-230, vert)
    vert += 30
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    for turtle_obj in all_turtle:
        if turtle_obj.xcor() > 200:  # the turtle. is necessary as it refers to the object of the item of the loop, without it the functions wouldn't know which object I mean xcor
            race_on = False
            winning_colour = turtle_obj.pencolor()
            if winning_colour == user_bet:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")

        rand_distance = randint(0, 10)
        turtle_obj.forward(rand_distance)

screen.exitonclick()
