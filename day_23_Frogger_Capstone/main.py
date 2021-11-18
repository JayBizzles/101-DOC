import turtle
from turtle import Turtle, Screen
from score import Score
from player import Player
from car import CarTool
import random

import time

game_state = True
screen = Screen()
screen.screensize(canvwidth=600, canvheight=600)
screen.tracer(0)

screen.listen()


score = Score()
player = Player()
cartool = CarTool()


print(player.position())
# #player controls
screen.onkeypress(fun=player.move, key= "w")

while game_state:
    difficulty = 6
    time.sleep(0.1)
    screen.update()

    cartool.car_creator(difficulty)
    cartool.move()

    for car in cartool.car_list:
        if car.distance(player) < 20:
            score.game_over()
            game_state = False
        elif player.distance(0, 300) < 20:
            score.increment()
            score.display()
            player.goto(0,-300)
            difficulty -= 1














screen.exitonclick()

###    Frogger Notes   ###


# main



# Car Class

## has c a color
## will use position

### given random color

# Player Class

## will use position
## move function

# Score Class

## Will be using self.write()
## number that increments