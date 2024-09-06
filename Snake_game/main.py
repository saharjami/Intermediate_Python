import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, key="Up")
screen.onkey(snake.go_down, key="Down")
screen.onkey(snake.go_left, key="Left")
screen.onkey(snake.go_right, key="Right")



end_of_game = False
while not end_of_game:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # end_of_game = True
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            # end_of_game = True
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()



screen.exitonclick()