from turtle import Turtle
START_POS = [(0, 0), (-10, 0), (-20, 0)]
STEP = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def add_seg(self, pos):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.shapesize(0.5)
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for seg_n in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_n - 1].xcor()
            y = self.segments[seg_n - 1].ycor()
            self.segments[seg_n].goto(x, y)
        self.head.forward(STEP)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(350, -400)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
