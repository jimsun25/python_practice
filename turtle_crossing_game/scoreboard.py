from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("Black")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(-230, 270)
        self.pendown()
        self.score = 1
        self.update()

    def update(self):
        show = f"Level: {self.score}"
        self.clear()
        self.write(arg=show, align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.write(arg="Game Over!", align="center", font=FONT)
