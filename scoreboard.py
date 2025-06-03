from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self ):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.L_score = 0
        self.R_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.L_score, align="center",font=("Courier", 70, "bold"))
        self.goto(100, 200)
        self.write(self.R_score, align="center",font=("Courier", 70, "bold"))

    def L_point(self):
        self.L_score += 1
        self.update_scoreboard()
    
    def R_point(self):
        self.R_score += 1
        self.update_scoreboard()
        
