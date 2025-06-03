from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle =Paddle(450,0)
l_paddle =Paddle(-450,0)
ball = Ball()
score = Scoreboard()




screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

game_is_on = True

while game_is_on:
    
    screen.update()
    ball.move()
    time.sleep(0.08)
    
    
             

    # Detect collision with the top and bottom walls 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with the right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 430:
        ball.paddle_bounce()
    # Detect collision with the left  Paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -430:
        ball.paddle_bounce()

    # Detect Right Paddle misses
    if ball.xcor() > 480 :
       ball.reset_position()
       score.L_point()

    # Detect Left Paddle misses
    if ball.xcor() < - 480 :
        ball.reset_position()
        score.R_point()
  



screen.exitonclick()