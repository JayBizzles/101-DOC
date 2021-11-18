from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time

# class Vector:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return 'Vector (%d, %d)' % (self.a, self.b)
#
#
# v1 = Vector(2,10)
# v2 = Vector(5,-2)
#
# print(v1)
#
# print(v2+v1)

# class Call:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     # def __str__(self):
#     #     return f"Call {self.a}, {self.b}"
#
# call = Call()
#
#
#
#
# a = 5
#
# b = 10
#
#
#
# print(a)
#
# print(b)


screen = Screen()
screen.screensize(canvwidth=400, canvheight=500)
screen.bgcolor("purple")
print(screen.screensize())

screen.listen()
scoreboard = Scoreboard()

game_state = True

player1 = Player()
player2 = Player()
ball = Ball()

player1.goto(-380, 0)
player2.goto(380, 0)


#player 1 controls
screen.onkeypress(fun=player1.move_up, key= "w")
screen.onkeypress(fun=player1.move_down, key= "s")

#player 2 controls
screen.onkeypress(fun=player2.move_up, key= "Up")
screen.onkeypress(fun=player2.move_down, key= "Down")


while game_state:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > float(200) or ball.ycor() < float(-200):
        ball.bounceup()

    if ball.distance(player2) <= 30:
        ball.bounceright()
    elif ball.distance(player1) <= 30:
        ball.bounceright()

    if ball.xcor() > 390:
        scoreboard.update_score_1()
        ball.home()
    elif ball.xcor() < -390:
        scoreboard.update_score_2()
        ball.home()

# make a scoreboard class
    # keeps score for both sides



# make a player class
    # have a paddle that can move

    # create another paddle for the opposite side


# make a ball class
    # ball can move

    # ball can detect collision with wall and bounces

    # ball can detect collision with paddle

    # can detect when a player misses



screen.exitonclick()