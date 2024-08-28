from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(40, 250)
        self.write(self.r_score, align='center', font=('Arial', 40, 'bold'))
        self.goto(-40, 250)
        self.write(self.l_score, align='center', font=('Arial', 40, 'bold'))

    def increase_l_score(self):
        self.l_score += 1
        self.update()

    def increase_r_score(self):
        self.r_score += 1
        self.update()

    # def game_over(self):
    #     self.color("red")
    #     self.goto(0, 0)
    #     self.write("Game Over", align="center", font=("Courier", 24, "normal"))