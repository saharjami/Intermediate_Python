from turtle import Turtle

POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_speed = 0.1

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self, coordinates):
        seg = Turtle(shape='square')
        seg.color('white')
        seg.shapesize(stretch_wid=1, stretch_len=1)
        self.segments.append(seg)
        seg.penup()
        seg.goto(coordinates)  # to place the segments next to each other

    def extend(self):
        self.add_segment(self.segments[-1].position())
        self.move_speed *= 0.9

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].xcor(), self.segments[i - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
