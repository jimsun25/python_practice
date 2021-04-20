from turtle import Turtle
FONT = ("Arial", 16, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("White")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.l_score = 0
        self.r_score = 0
        self.update("start")

    def update(self, lost):
        if lost == "left":
            self.r_score += 1
        if lost == "right":
            self.l_score += 1
        show = f"{self.l_score}    Score    {self.r_score}"
        self.clear()
        self.write(arg=show, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over!", align="center", font=FONT)
