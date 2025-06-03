from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,x_position,y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.penup()
        self.goto(x_position,y_position)

    def move_up(self):
        self.fd(35)
 
    def move_down(self):
        self.back(35)
        