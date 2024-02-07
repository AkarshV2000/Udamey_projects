import colorgram
import turtle as t
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")



colors = colorgram.extract('image.jpg', 20)
print(colors)

# screen = Screen()
# screen.exitonclick()
# cant make thos project since image import is not working