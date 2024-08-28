from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()



    def update_level(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f'Level: {self.level}', align='center', font=('Courier', 24))

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", align='center', font=('Courier', 24))