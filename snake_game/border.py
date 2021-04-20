from turtle import Turtle
FONT = ("Arial", 12, "normal")


class Border(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("White")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(-296, 280)
        self.pendown()
        self.pensize(4)
        self.setheading(0)

        self.forward(586)
        self.right(90)
        self.forward(585)
        self.right(90)
        self.forward(586)
        self.right(90)
        self.forward(585)
        self.right(90)

