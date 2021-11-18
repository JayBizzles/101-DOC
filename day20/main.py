from turtle import Screen
import time
from snake_game import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.screensize(canvheight=400, canvwidth=500)
screen.bgcolor("black")

screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_down, "Down")

while snake.game_state:
    screen.update()
    time.sleep(0.2)

    print(screen.canvheight)

    print("#"*10)
    snake.move()
    print("#" * 10)
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.set_val()
        scoreboard.add_point()
        snake.add_to_tail()

    #detect collision with wall
    if abs(snake.head.xcor()) >= screen.canvwidth-20:
        scoreboard.reset()
        snake.reset()
    elif abs(snake.head.ycor()) >= screen.canvheight:
        scoreboard.reset()
        snake.reset()



    # detect collision with tail
    for snaketail in snake.snakelist[1:]:
        if snake.head.distance(snaketail) < 10:
            scoreboard.reset()
            snake.reset()


scoreboard.clear()


screen.exitonclick()