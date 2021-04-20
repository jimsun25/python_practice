from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.goto(pos)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)
