from turtle import Turtle, Screen
import time
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # if player.ycor()>=280:
    #     game_is_on = False

screen.exitonclick()
