import time
from food import Food
from turtle import *
from Snake import Snake
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Scoreboard()

x = 0
screen.onkey(snake.up, 'w')
screen.onkey(snake.east, 'd')
screen.onkey(snake.west, 'a')
screen.onkey(snake.down, 's')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with walls
    if snake.head.xcor() > 300 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300:
        game_on = False
        scoreboard.game_over()

    # detect collision with tail.
    for segment in snake.parts[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
