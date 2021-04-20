from turtle import Turtle, Screen
import random


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    return color


tim = Turtle()
tim.shape("turtle")
tim.color("midnight blue")
tim.pensize(1)
tim.speed(50)
directions = [0, 90, 180, 270]

# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()

# for n in range(3, 11):
#     tim.pencolor(random_color())
#     for _ in range(n):
#         tim.forward(50)
#         tim.right(360/n)

# for n in range(500):
#     tim.pencolor(random_color())
#     tim.forward(20)
#     tim.setheading(random.choice(directions))

circle_number = 100
for _ in range(circle_number):
    tim.pencolor(random_color())
    tim.circle(150)
    tim.left(360 / circle_number)








screen = Screen()
screen.exitonclick()