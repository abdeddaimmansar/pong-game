from turtle import Turtle, Screen
from ball import Ball
import time
from scoreboard import  ScoreBoard

from paddle import Paddle

my_screen = Screen()
my_screen.title("Pong-Game")
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()
my_screen.listen()
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "s")
my_screen.onkey(l_paddle.go_down, "w")

game_on = True
speed = 0.1
while game_on:
    # ball.move()
    my_screen.update()
    time.sleep(speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
        speed *=0.5
    if ball.xcor() > 380:
        score.r_increase()
        ball.start()
        speed = 20

    if ball.xcor() < - 380:
        score.l_increase()
        speed = 0.1

        ball.start()

my_screen.exitonclick()
