import time
import random
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
generate_loops = 10
while game_is_on:
    time.sleep(0.05)
    if random.randint(0, generate_loops) == 0:
        car_manager.generate_car()
        loop_count = 0
    car_manager.move_cars()
    if car_manager.detect_collision(player):
        game_is_on = False
        scoreboard.game_over()
    if player.ycor() > FINISH_LINE_Y:
        player.restart()
        car_manager.increase_speed()
        scoreboard.update()
        if generate_loops > 1:
            generate_loops = int(generate_loops * 0.9)

    screen.update()

screen.exitonclick()
