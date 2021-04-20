from turtle import Turtle, Screen
import random
race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-75, -45, -15, 15, 45, 75]
turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos[i])
    turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:

    cur_turtle = random.choice(turtles)
    cur_turtle.forward(random.randint(0, 5))
    if cur_turtle.xcor() > 230:
        race_on = False
        win = cur_turtle.pencolor()
        if win == user_bet:
            print("You've won the bet!!!")
        else:
            print(f"You've lost. The {win} turtle is the winner.")


screen.exitonclick()