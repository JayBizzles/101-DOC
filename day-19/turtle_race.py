import turtle
from turtle import Turtle, Screen
import random

colorlist = ["blue", "green", "yellow", "black", "red", "purple", "orange"]
turtlelist = {}

screen = Screen()



screen.setup(width=500, height=400)


numplayers = round(screen.numinput("How many challengers?", "Enter the num of turtles"))

for i in range(numplayers):
    tname = screen.textinput("wtfthisdo", "input name:")
    turtlelist[tname] = None

for turtle in turtlelist.keys():
    turtlelist[turtle] = Turtle(shape="turtle")
    turtlelist[turtle].color(colorlist.pop())


print(turtlelist)

# put turtles in racing position

# have to make the finish line

def turtle_lineup(turtlelist):
    valy = 180

    for turtle_name, turtle_obj in turtlelist.items():
        turtle_obj.penup()
        turtle_obj.goto(-240, valy)
        valy -= 50


# then we have to keep adding until we get to the end of the screen

# after that we return who won
def move(turtlelist):
    racing = True
    while racing:
        for turtle_name, turtle_obj in turtlelist.items():
            fval = random.randint(1,10)
            turtle_obj.forward(fval)
            if round(turtle_obj.xcor()) >= 230:
                racing = False
                break
    return turtle_name








turtle_lineup(turtlelist)
winner = move(turtlelist)

print(f"Fastest Turtle: {winner}")
screen.exitonclick()