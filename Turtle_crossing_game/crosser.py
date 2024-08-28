from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
class Crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def start_over(self):
        self.goto(STARTING_POSITION)