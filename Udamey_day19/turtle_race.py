from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width= 600, height= 400)
user_bet = screen.textinput(title="Make you bet", prompt= " Which turtle would win the race? pick our colour: " )
colors = ["red" , "orange"  , "green" , "orange", "blue", "purple"]
y_position = [-100, -60 , -20 , 20 , 60, 100]
all_turtle = []


for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -290, y = y_position[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for x in all_turtle:
# i am not getting how x in inherting all the properties of Turtle class
# Maybe its bc of x in looping through a list of objects of Turtle class 
        if x.xcor() > 280:
            is_race_on = False
            winning_color = x.pencolor()
            if winning_color == user_bet:
                print(f"you won! {winning_color} turtle won the race")
            else:
                print(f"You lost! {winning_color} trutle won the race ")
            
        random_distance = random.randint(0,10)
        x.forward(random_distance)


screen.exitonclick()