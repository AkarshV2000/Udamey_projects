###  Differentways of importing  ###

#1 --> import turtle 
#       THis will import the entire thing but to create any object you have to write it like
#        screen = turtle.Screen() or timmy = turtle.Turtle()
#        importing like this is fine but if you have create lots of object from same class then
#        its not the best way since you always have to type "turtle."
#
#2--> from turtle import Turtle, Screen
#     THis meths id mostly used when you have to work with particular classes instead of the 
#     whole code snippet
#
#3 --> import turtle as t
#      screen = t.Screen()
#      if the file name is too long you can just import it with an alias for the ease of code
#
#4 --> There are tons of libraries that you can import but not directly via importing ,
#      since they dont come with python package, instead go to "pypi.org" look for the suitable
#      library you want to use and install it via your termina "pip install (package name)"


from turtle import Turtle, Screen
import turtle as t


timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")


#--> Timmy  is moving and skipping basically creating a dashed line
# for _ in range(15):
# #--> The underscore (_) is typically used as a throwaway variable or a placeholder 
# #     when the variable itself is not going to be used in the loop body. In this specific loop
    
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


#--> Timmy is drawing some shapes in below program

# def draw_shape(sides):
#     angle = int(360/sides)
#     for _ in range(sides):
#         timmy.right(angle)
#         timmy.forward(50)

# for i in range(3,11):
#     draw_shape(i)

#--> Timmy's drunk, hes moving on random path with different colors

import random

# Creating a random rgb color, so we canget rid of that colors list
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g ,b)
    return color
# colours = [ 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 
#           "SeaGreen", 'darkred', 'darksalmon', 'darkseagreen', 
#         'darkslateblue', 'darkslategray', 'darkturquoise', 'darkviolet',
#         'deeppink', 'deepskyblue', 'dodgerblue', 'firebrick', 'forestgreen',
#         'gold', 'goldenrod', 'green', 'hotpink', 'indianred', 'khaki','maroon', 
#         'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 
#          'darkgray', 'darkgreen', 'darkkhaki', 'darkmagenta', 'darkolivegreen',
#         'darkorange', 'darkorchid', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 
#         'salmon', 'sandybrown', 'seagreen', 'seashell' ]

# direction = [0,90,180,270]
timmy.pensize(2)
timmy.speed(15)
# for _ in range(1000):
#     timmy.pencolor(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))


#--> Drawing a beautiful spirograph
def draw_a_spirogaph(gap_value):

    for _ in range(int(360/gap_value)):
        timmy.color(random_color())
        timmy.circle(100)
        current_heading = timmy.heading()
        timmy.setheading(current_heading+ gap_value)
draw_a_spirogaph(5)



screen = Screen()
screen.exitonclick()


