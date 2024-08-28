from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

paddle_pos = [(360, 0), (-360, 0)]

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(paddle_pos[0])
l_paddle = Paddle(paddle_pos[1])
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, key="Up")
screen.onkey(r_paddle.go_down, key="Down")
screen.onkey(l_paddle.go_up, key="w")
screen.onkey(l_paddle.go_down, key="s")


end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(0.03)
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.shoot()
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.increase_l_score()
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.increase_r_score()

screen.exitonclick()