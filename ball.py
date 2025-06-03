from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_update = 9
        self.y_update = 7
        self.move_speed = 0.1

        # self.setheading(30)

    def move(self):
        """"""
        new_x = self.xcor() + self.x_update
        new_y = self.ycor() + self.y_update
        # update new postion 
        self.goto(new_x,  new_y)
        # self.setheading(30)
        # self.fd(25)

    def bounce(self):
        self.y_update *= -1

    def paddle_bounce(self):
        self.x_update *= -1
        self.move_speed *= 0.7

    def reset_position(self):
        self.goto(0, 0)
        self.paddle_bounce()
        self.move_speed = 0.1
        
