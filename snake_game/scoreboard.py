from turtle import Turtle
FONT = ("Arial", 12, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.pencolor("White")
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(150, 288)
        self.pendown()
        self.score = -1
        with open("high_score.txt") as file:
            history = int(file.read())
        self.high_score = history
        self.update()

    def update(self):
        self.score += 1
        show = f"Score: {self.score}          High Score: {self.high_score}"
        self.clear()
        self.write(arg=show, align="center", font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over!", align="center", font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as note:
                note.write(str(self.high_score))
        self.score = -1
        self.update()

    # def ask_restart(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.pendown()
    #     self.write(arg="Press 'Enter' to restart", align="center", font=FONT)
    #     self.penup()
    #     self.goto(150, 288)
    #     self.pendown()
