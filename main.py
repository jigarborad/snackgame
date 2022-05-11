import time
from turtle import Turtle, Screen

import snack
from food import Food
from scoreboard import Scoreboard
from snack import Snack
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")
game_is_on = True
i=2
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()

    # collision with food
    if snack.head.distance(food) < 15:
        food.refresh()
        scoreboard.score_count()
        snack.add_segment()

    # detect collision with wall
    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        scoreboard.reset()
        snack.reset()

    # collision with tail
    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 10:
            scoreboard.reset()
            snack.reset()
screen.exitonclick()

