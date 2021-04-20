from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.2, 0.2)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-283, 283)
        y = random.randint(-297, 257)
        self.goto(x, y)
