from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    def __init__(self):
        self.car_list = []
        self.cur_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.shape("square")
        new_car.setheading(180)
        new_car.turtlesize(stretch_len=2, stretch_wid=1)
        new_car.color(random.choice(COLORS))
        new_car.goto(x=320, y=random.randint(-240, 240))
        self.car_list.append(new_car)

    def move_cars(self):
        for car in self.car_list:
            car.forward(self.cur_speed)
            if car.xcor() < -340:
                self.car_list.remove(car)

    def detect_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:
                return True

    def increase_speed(self):
        self.cur_speed += MOVE_INCREMENT
