from turtle import Screen , Turtle

POSITIONS= [(350,0), (-350,0)]
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(4,1,4)
        self.penup()
        self.goto(position)
        self.new_y = 0


    def go_up(self):
        new_y = self.ycor()+ 20
        self.goto(self.xcor(), new_y)
        
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

