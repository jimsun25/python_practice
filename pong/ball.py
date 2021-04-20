from turtle import Turtle
STARTHEADING = 45

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.setheading(STARTHEADING)
        self.movespeed = 0.05

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        cur_angle = self.heading()
        self.setheading(360-cur_angle)

    def bounce_paddle(self):
        cur_angle = self.heading()
        self.setheading(540-cur_angle)
        self.movespeed *= 0.9

    def restart(self, direction):
        self.goto(0, 0)
        self.movespeed = 0.05
        if direction == "left":
            self.setheading(45)
        if direction == "right":
            self.setheading(225)


