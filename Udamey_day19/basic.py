from turtle import Turtle, Screen

timmy = Turtle()
tommy = Turtle()
Brew = Turtle()
#--> here we are creating different instances from a same class, they have their 
#    seperate state and functions they'll perform
 
screen = Screen()

# Below we created a function move forward and used it as an argument for onkey
def move_forward():
    timmy.forward(10)
screen.listen() # We cal this method in case of any input to be given
#-->  while passing a function as an argument we do not need to use parenthesis
# whenever we will press space it will call upon the function move_forward
screen.onkey(move_forward,"space") 
screen.exitonclick()

