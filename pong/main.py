from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_pd = Paddle((350, 0))
l_pd = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_pd.up, "Up")
screen.onkey(r_pd.down, "Down")
screen.onkey(l_pd.up, "w")
screen.onkey(l_pd.down, "s")


game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    if 320 < ball.xcor() < 340 and ball.distance(r_pd) < 50:
        ball.bounce_paddle()
    if -340 < ball.xcor() < -320 and ball.distance(l_pd) < 50:
        ball.bounce_paddle()
    if ball.xcor() > 380:
        ball.restart("right")
        scoreboard.update("right")
        time.sleep(0.05)
    if ball.xcor() < -380:
        ball.restart("left")
        scoreboard.update("left")
        time.sleep(0.05)
    ball.move()



screen.exitonclick()