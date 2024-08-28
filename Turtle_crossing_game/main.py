import random
from turtle import Screen
import time
import random
from scoreboard import Scoreboard
from crosser import Crosser
from cars import Cars


y_pos = [-250, -200, -150, -100, -50, 0, 50, 100, 150, 200, 250]

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

scoreboard = Scoreboard()
crosser = Crosser()
cars = Cars()



screen.listen()
screen.onkey(crosser.move, "Up")


end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_level()
    cars.create_car()
    cars.move_cars()
    for car in cars.all_cars:
        if crosser.distance(car) < 20:
            scoreboard.game_over()
            end_of_game = True
    if crosser.ycor() > 250:
        scoreboard.increase_level()
        crosser.start_over()
        cars.increase_speed()

screen.exitonclick()
