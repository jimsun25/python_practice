from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from border import Border
import time
BORDER = 10

screen = Screen()
screen.setup(width=600, height=630)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

border = Border()
snake = Snake()
food = Food()
sb = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 10:
        food.refresh()
        sb.update()
        snake.extend()

    # detect wall collision
    if snake.head.xcor() > 299 - BORDER or snake.head.ycor() > 289 - BORDER or\
            snake.head.xcor() < -300 + BORDER or snake.head.ycor() < -315 + BORDER:
        sb.reset_score()
        snake.reset_snake()

    # detect tail collision
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 6:
            sb.reset_score()
            snake.reset_snake()

screen.exitonclick()
