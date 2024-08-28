from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        self.penup()
        x = randint(-250, 250)
        y = randint(-250, 250)
        self.goto(x, y)
